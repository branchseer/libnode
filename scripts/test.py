assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

os.chdir('test')
shutil.rmtree('build', ignore_errors=True)
os.mkdir('build')
os.chdir('build')
if sys.platform == 'win32':
    subprocess.check_call(['cmake', '-G', 'Visual Studio 15 2017', '-A', ('Win32' if config.x86 else 'x64'), '-S', '..'])
else:
    subprocess.check_call(['cmake', '-G', 'Unix Makefiles', '-DCMAKE_BUILD_TYPE=Release', '-S', '..'])

subprocess.check_call(['cmake', '--build', '.', '--config', 'Release'])


exec_path = 'Release\\libnode_test.exe' if sys.platform == 'win32' else './libnode_test'
output_version = subprocess.check_output([exec_path, '-e', 'console.log(process.version)']).decode()
assert output_version.strip() == config.nodeVersion
