assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

shutil.rmtree('build', ignore_errors=True)
os.mkdir('build')
os.chdir('build')
if sys.platform == 'win32':
    subprocess.check_call(['cmake', '-G', 'Visual Studio 15 2017', '-A', ('Win32' if config.x86 else 'x64'), '-S', '../src'])
else:
    subprocess.check_call(['cmake', '-G', 'Unix Makefiles', '-DCMAKE_BUILD_TYPE=Release', '-S', '../src'])
os.chdir('..')

subprocess.check_call(['cmake', '--build', 'build', '--config', 'Release'])


os.chdir('node-{}'.format(config.nodeVersion))

if sys.platform == 'win32':
    vcbuildArgs = [ 'static' ]
    if config.x86:
        vcbuildArgs.append('x86')

    env = os.environ.copy()
    env['config_flags'] = ' '.join(config.configFlags)
    
    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat'] + vcbuildArgs,
        env=env
    )
else:
    configureArgvs = ['./configure', '--enable-static']
    if config.configFlags is not None:
        configureArgvs += config.configFlags
    subprocess.check_call(configureArgvs)
    subprocess.check_call(['make', '-j{}'.format(os.cpu_count())])
