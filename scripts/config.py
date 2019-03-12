assert __name__ != "__main__"

import os

nodeVersion = "v11.11.0"
configFlags = os.environ.get('libnode_config_flags')
x86 = os.environ.get('libnode_x86') == '1'
zipBasenameSuffix = os.environ.get('libnode_zip_suffix', '')
