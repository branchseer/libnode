assert __name__ != "__main__"

import os

nodeVersion = os.environ['LIBNODE_NODE_VERSION']
configFlags = (os.environ.get('LIBNODE_CONFIG_FLAGS') or '').split()
x86 = os.environ.get('LIBNODE_X86') == '1'
zipBasenameSuffix = os.environ.get('LIBNODE_ZIP_SUFFIX', '')

if os.environ.get('LIBNODE_SMALL_ICU', '') == '1':
	configFlags += ['--with-intl=small-icu']
	zipBasenameSuffix += '-smallicu'
