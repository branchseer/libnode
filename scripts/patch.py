from . import config
import os
import subprocess
from distutils.dir_util import copy_tree

os.chdir('node-{}'.format(config.nodeVersion))

copy_tree('../patch/node', '.')
subprocess.check_call(['patch', '-p1', '-i', '../patch/node.patch'])
