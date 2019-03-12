# libnode

This repo contains the scripts that build [Node.js](http://nodejs.org/) as a static library for embedding in [DeskGap](https://deskgap.com/).

## Usage

### Downloading the source code of Node.js:
```sh
python3 -m scripts.download
```

### Configuring (optional):

#### Remove `Intl` support to reduce the size:
```sh
export LIBNODE_CONFIG_FLAGS=--without-intl
export LIBNODE_ZIP_SUFFIX=-nointl
```

#### Build the x86 version (Windows only):
```sh
export LIBNODE_X86=1
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
