# libnode

This repo contains the scripts that build [Node.js](http://nodejs.org/) as a static library for embedding in [DeskGap](https://deskgap.com/).

## Usage

### Configuring

#### Specify the Node version:
```sh
export LIBNODE_NODE_VERSION=v11.11.0
```

#### Remove `Intl` support to reduce the size (optional):
```sh
export LIBNODE_CONFIG_FLAGS=--without-intl
export LIBNODE_ZIP_SUFFIX=-nointl
```

#### Build the x86 version (optional, Windows only):
```sh
export LIBNODE_X86=1
```

### Downloading the source code of Node.js:
```sh
python3 -m scripts.download
```

### Building Node.js:
```sh
python3 -m scripts.build
```

### Archiving the static library:
```sh
python3 -m scripts.postproc
python3 -m scripts.archive
```
