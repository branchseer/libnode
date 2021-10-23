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
    subprocess.check_call(['cmake', '-G', 'Visual Studio 16 2019', '-A', ('Win32' if config.x86 else 'x64'), '-S', '..'])
else:
    subprocess.check_call(['cmake', '-G', 'Unix Makefiles', '-DCMAKE_BUILD_TYPE=Release', '-S', '..'])

subprocess.check_call(['cmake', '--build', '.', '--config', 'Release'])

tests = [
#    executable args expected_output
    ["simple", ["console.log(require('http').STATUS_CODES[418])"], ["I'm a Teapot", "exit code: 0"]],
    ["simple", ["process.exit(12)"], ["exit code: 12"]],
    ["simple", ["invalid javascript"], ["napi_run_script failed", "exit code: 1"]],
    ["process_argv", [], ["hello node", "exit code: 0"]],
]

failed = False

for test in tests:
    [exec_name, args, expected_output] = test
    exec_path = f'Release\\{exec_name}.exe' if sys.platform == 'win32' else f'./{exec_name}'
    output = subprocess.check_output([exec_path] + args).decode().strip().splitlines()
    if output != expected_output:
        print("Assertion Failed. Expected:", expected_output, "Actual:", output)
        failed = True

if failed:
    exit(1)

