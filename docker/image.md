# PyMesh Docker Image

## What this image is for

This image provides a ready-to-run **PyMesh** environment for geometry processing in Python, without requiring local compilation of dependencies.

Use it to:

- run PyMesh scripts in a clean container,
- test mesh workflows consistently across machines,
- validate builds in CI.

## What is included

- Python 3.13 runtime
- `pymesh` Python package (built from this repository)
- Core Python deps: `numpy`, `scipy`
- Runtime system libraries required by PyMesh
- Basic shell utilities (`bash`, `curl`, `less`, `procps`, `file`)

The final image contains runtime artifacts only (no source tree or build intermediates).

## Quick start

Pull and open a shell:

```bash
docker run --rm -it quantecdc/pymesh:1.0 bash
```

Verify import:

```bash
docker run --rm -it quantecdc/pymesh:1.0 \
  bash -lc "python -c 'import pymesh; print(\"pymesh ok\")'"
```

Mount local files:

```bash
docker run --rm -it -v "$PWD:/workspace" quantecdc/pymesh:1.0 bash
```
