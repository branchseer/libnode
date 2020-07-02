from . import config
import os
import subprocess

os.chdir('node-{}'.format(config.nodeVersion))

subprocess.check_call(['patch', '-p1', '-i', '../node_start.patch'])
