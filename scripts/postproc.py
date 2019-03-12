assert __name__ == "__main__"

import sys
import os
import shutil
import subprocess

from . import config

nodeSrcFolder = 'node-{}'.format(config.nodeVersion)
resultFolder = 'release'

try:
    os.rmdir(resultFolder)
except:
    pass

os.mkdir(resultFolder)

def filterLibFile(filename):
    return 'gtest' not in filename and 'v8_nosnapshot' not in filename

if sys.platform == 'win32':
    for libFile in os.scandir(nodeSrcFolder + '\\Release\\lib'):
        if libFile.is_file() and libFile.name.endswith('.lib') and filterLibFile(libFile.name):
            print('Copying', libFile.name)
            shutil.copy(libFile.path, resultFolder)
elif sys.platform == 'darwin':
    for libFile in os.scandir(nodeSrcFolder + '/out/Release'):
        if libFile.is_file() and libFile.name.endswith('.a') and filterLibFile(libFile.name):
            print('Copying', libFile.name)
            shutil.copy(libFile.path, resultFolder)
            print('Striping', libFile.name)
            subprocess.check_call(['strip', '-x', os.path.join(resultFolder, libFile.name)])
elif sys.platform == 'linux':
    for dirname, _, basenames in os.walk(nodeSrcFolder + '/out/Release/obj.target'):
        for basename in basenames:
            if basename.endswith('.a') and filterLibFile(basename):
                subprocess.run(
                    'ar -t {} | xargs ar rs {}'.format(
                        os.path.join(dirname, basename),
                        os.path.join(resultFolder, basename)
                    ),
                    check=True, shell=True
                )
