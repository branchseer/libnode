assert __name__ == "__main__"

import sys
import os
import subprocess

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

if sys.platform == 'win32':
    vcbuildArgs = [ 'static', 'openssl-no-asm' ]
    if config.x86:
        vcbuildArgs.append('x86')

    env = os.environ.copy()
    if config.configFlags is not None:
        env['config_flags'] = config.configFlags
    
    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat'] + vcbuildArgs,
        env=env
    )
else:
    configureArgvs = ['./configure', '--enable-static']
    if config.configFlags is not None:
        configureArgvs.append(config.configFlags)
    subprocess.check_call(configureArgvs)
    subprocess.check_call(['make', '-j{}'.format(os.cpu_count())])
