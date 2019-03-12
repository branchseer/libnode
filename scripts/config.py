assert __name__ != "__main__"

import os

nodeVersion = "v11.11.0"
configFlags = os.environ.get('LIBNODE_CONFIG_FLAGS')
x86 = os.environ.get('LIBNODE_X86') == '1'
zipBasenameSuffix = os.environ.get('LIBNODE_ZIP_SUFFIX', '')
