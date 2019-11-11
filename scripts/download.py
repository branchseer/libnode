assert __name__ == "__main__"

import urllib.request
import tarfile
import os
import subprocess

from . import config

subprocess.check_call(['choco', 'install', 'nasm', '-y'])

url = 'https://nodejs.org/dist/{}/node-{}.tar.gz'.format(config.nodeVersion, config.nodeVersion)
header_url = "https://nodejs.org/dist/{}/node-{}-headers.tar.gz".format(config.nodeVersion, config.nodeVersion)

print('Downloading...')
urllib.request.urlretrieve(url, filename="node_src.tar.gz")
urllib.request.urlretrieve(header_url, filename="node_headers.tar.gz")

print("Extracting...")
with tarfile.open('node_src.tar.gz') as srcTarball:
    srcTarball.extractall()
with tarfile.open('node_headers.tar.gz') as headersTarball:
    headersTarball.extractall()

os.remove('node_src.tar.gz')
os.remove('node_headers.tar.gz')
