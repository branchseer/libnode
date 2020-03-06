assert __name__ == "__main__"

import subprocess
import os
import shutil

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

subprocess.check_call(['patch', '-p1', '-i', '../uv.patch'])
shutil.copyfile('deps/uv/include/uv.h', 'include/node/uv.h')
