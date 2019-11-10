assert __name__ != "__main__"

import os

nodeVersion = os.environ['LIBNODE_NODE_VERSION']
configFlags = [] if ('LIBNODE_CONFIG_FLAGS' not in os.environ) else os.environ['LIBNODE_CONFIG_FLAGS'].split()
x86 = os.environ.get('LIBNODE_X86') == '1'
zipBasenameSuffix = os.environ.get('LIBNODE_ZIP_SUFFIX', '')
