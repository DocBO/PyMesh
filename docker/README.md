# Docker

This folder contains a single versatile multi-stage Docker build for PyMesh.

## Goals

- Build on a slim Ubuntu base.
- Keep bash and common CLI tools in runtime.
- Remove all source/build artifacts from the final image.
- Keep only runtime Python dependencies and the installed `pymesh` module.

## Build

From repository root:

```bash
./docker/build.sh
```

Optional arguments:

```bash
IMAGE_NAME=pymesh/pymesh:dev UBUNTU_VERSION=22.04 RUN_TESTS=1 ./docker/build.sh
```

## Runtime

The final image includes:

- `python3`, `pip`, `bash`
- Useful tools: `curl`, `less`, `procps`, `file`
- Installed Python packages: `pymesh`, `numpy`, `scipy`
- Required shared runtime libraries (`libstdc++`, GMP/MPFR, TBB, OpenMP)

No source tree or intermediate compilation artifacts are copied into the final stage.
