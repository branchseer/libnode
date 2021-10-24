from . import config
import os
import subprocess
import shutil

os.chdir('node-{}'.format(config.nodeVersion))

shutil.copytree('../patch/node', '.', dirs_exist_ok=True)
subprocess.check_call(['patch', '-p1', '-i', '../patch/node.patch'])
