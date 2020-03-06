assert __name__ == "__main__"

import subprocess

from . import config

subprocess.check_call(['patch', '-d', 'node-{}'.format(config.nodeVersion), '-p1', '-i', '../uv.patch'])
