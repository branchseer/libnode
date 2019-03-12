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
    
    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat'] + vcbuildArgs,
        env={ **os.environ, 'config_flags': config.configFlags }
    )
else:
    subprocess.check_call(['./configure', '--enable-static'] + [config.configFlags])
    subprocess.check_call(['make', '-j{}'.format(os.cpu_count())])
