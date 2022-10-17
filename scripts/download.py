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
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(srcTarball)

os.remove('node_src.tar.gz')
