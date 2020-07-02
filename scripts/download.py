assert __name__ == "__main__"

import urllib.request
import tarfile
import os
import subprocess

from . import config


url = 'https://nodejs.org/dist/{}/node-{}.tar.gz'.format(config.nodeVersion, config.nodeVersion)

print('Downloading...')
urllib.request.urlretrieve(url, filename="node_src.tar.gz")

print("Extracting...")
with tarfile.open('node_src.tar.gz') as srcTarball:
    srcTarball.extractall()

os.remove('node_src.tar.gz')
