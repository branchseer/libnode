assert __name__ == "__main__"

import subprocess
import os
import shutil

from . import config

baseDir = os.getcwd() + '/node-{}'.format(config.nodeVersion) 
subprocess.check_call(['patch', '-d', baseDir, '-p1', '-i', '../uv.patch'])


print(os.listdir(baseDir))
print(os.listdir(baseDir + '/include/node'))


shutil.copyfile(baseDir + '/deps/uv/include/uv.h', baseDir + '/include/node/uv.h')
