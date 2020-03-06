assert __name__ == "__main__"

import urllib.request
import tarfile
import os
import subprocess

from . import config


url = 'https://nodejs.org/dist/{}/node-{}.tar.gz'.format(config.nodeVersion, config.nodeVersion)
header_url = "https://nodejs.org/dist/{}/node-{}-headers.tar.gz".format(config.nodeVersion, config.nodeVersion)
patch_url = 'https://github.com/electron/electron/raw/39baf6879011c0fe8cc975c7585567c7ed0aeed8/patches/node/feat_add_uv_loop_watcher_queue_code.patch'


print('Downloading...')
urllib.request.urlretrieve(url, filename="node_src.tar.gz")
urllib.request.urlretrieve(header_url, filename="node_headers.tar.gz")
urllib.request.urlretrieve(patch_url, filename="uv.patch")

print("Extracting...")
with tarfile.open('node_src.tar.gz') as srcTarball:
    srcTarball.extractall()
with tarfile.open('node_headers.tar.gz') as headersTarball:
    headersTarball.extractall()

os.remove('node_src.tar.gz')
os.remove('node_headers.tar.gz')
