assert __name__ == "__main__"

import sys
import os
import subprocess

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

subprocess.check_call([ sys.executable, 'tools/install.py', 'install', '.', '' ], env={ 'HEADERS_ONLY': '1' })
