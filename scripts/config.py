assert __name__ != "__main__"

import os

nodeVersion = os.environ.get['LIBNODE_NODE_VERSION']
configFlags = (os.environ.get('LIBNODE_CONFIG_FLAGS') or '').split()
x86 = os.environ.get('LIBNODE_X86') == '1'
zipBasenameSuffix = os.environ.get('LIBNODE_ZIP_SUFFIX', '')

if os.environ.get('LIBNODE_NO_INTL', '') == '1':
	configFlags += ['--without-intl']
	zipBasenameSuffix += ['-nointl']
