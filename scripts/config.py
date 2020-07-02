assert __name__ != "__main__"

import os

nodeVersion = os.environ.get('LIBNODE_NODE_VERSION') or '14.5.0'
configFlags = [] if ('LIBNODE_CONFIG_FLAGS' not in os.environ) else os.environ['LIBNODE_CONFIG_FLAGS'].split()
x86 = os.environ.get('LIBNODE_X86') == '1'
zipBasenameSuffix = os.environ.get('LIBNODE_ZIP_SUFFIX', '')
