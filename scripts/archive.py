assert __name__ == "__main__"

import shutil
import sys

from . import config

zipBasename = 'libnode-{}-{}-{}{}'.format(
    config.nodeVersion,
    sys.platform,
    'x86' if config.x86 else 'x64',
    config.zipBasenameSuffix
)

shutil.make_archive(zipBasename, 'zip', base_dir='libnode')

print(zipBasename + '.zip')
