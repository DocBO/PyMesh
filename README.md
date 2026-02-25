[![CircleCI](https://circleci.com/gh/PyMesh/PyMesh/tree/main.svg?style=svg)](https://circleci.com/gh/PyMesh/PyMesh/tree/main)
[![Documentation Status](https://readthedocs.org/projects/pymesh/badge/?version=latest)](https://pymesh.readthedocs.io/en/latest/?badge=latest)

### About PyMesh ###

**PyMesh** is a geometry-processing toolkit with a C++ computational core and a
Python API layer.

Current architecture:

- Core mesh data structures and algorithms are implemented in `src/` and `tools/`.
- Python bindings are built with **pybind11** from `python/`.
- Optional third-party backends (CGAL, libigl, TetGen, Triangle, MMG, Draco,
  etc.) are compiled from `third_party/` and linked into the same Python module.
- Backend selection is runtime-configurable in Python (for example boolean,
  triangulation, tetrahedralization, winding number engines).

![PyMesh][teaser]
(Model source: [Bust of Sappho](https://www.thingiverse.com/thing:14565))

### Documentation ###

[Latest documentation](https://pymesh.readthedocs.io/en/latest/)

### Documentation HOWTO

Build docs locally:

```bash
cd $PYMESH_PATH
python3 -m pip install sphinx
make -C docs html
```

Generated site:

- `docs/_build/html/index.html`

Useful checks:

```bash
# Fail on warnings in CI
make -C docs clean
make -C docs html SPHINXOPTS="-W --keep-going"

# External link validation
make -C docs linkcheck
```

Preview locally in a browser:

```bash
cd $PYMESH_PATH/docs/_build/html
python3 -m http.server 8000
```

Then open `http://127.0.0.1:8000`.

Clean and rebuild from scratch:

```bash
make -C docs clean
make -C docs html
```

### Repository Layout ###

- `src/`: core mesh library (geometry, IO, attributes, connectivity).
- `tools/`: algorithm engines (boolean, triangulation, tetrahedralization,
  convex hull, winding number, etc.).
- `python/`: pybind11 module sources and high-level `pymesh` Python package.
- `tests/`: C++ unit tests and test data.
- `third_party/`: vendored dependencies and build scripts.

### Download Source ###

```bash
git clone https://github.com/PyMesh/PyMesh.git
cd PyMesh
git submodule update --init --recursive
```

### Dependencies ###

Required runtime:

- [Python](https://www.python.org/) **3.13+**
- [NumPy](http://www.numpy.org/)
- [SciPy](http://www.scipy.org/)

Required build tooling/libraries (Linux):

- `build-essential`, `cmake`, `python3-dev`
- `libeigen3-dev`, `libgmp-dev`, `libgmpxx4ldbl`, `libmpfr-dev`
- `libboost-dev`, `libboost-thread-dev`, `libtbb-dev`

Most optional geometry libraries are included as submodules under
`third_party/` and are built locally.

### Build ###

Let `$PYMESH_PATH` be the repository root.

1. Build third-party dependencies:

```bash
cd $PYMESH_PATH/third_party
./build.py all
```

2. Configure and build PyMesh:

```bash
cd $PYMESH_PATH
mkdir -p build
cd build
cmake .. -DPython_EXECUTABLE=$(which python)
make -j$(nproc)
make tests
```

### Python Test Run ###

Run Python-side tests against the in-repo package:

```bash
cd $PYMESH_PATH
python3 -c "import sys; sys.path.insert(0, 'python'); import pymesh; r=pymesh.test(verbosity=1); import sys as _s; _s.exit(0 if r.wasSuccessful() else 1)"
```

### Install ###

```bash
cd $PYMESH_PATH
./setup.py build
./setup.py install --user
```

### Feedback ###

Thank you for using PyMesh. Please consider leaving [feedback][feedback].

[teaser]: docs/_static/pymesh_teaser.jpg
[feedback]: https://docs.google.com/forms/d/e/1FAIpQLSc8YAzx1SL4t3qntzahYd0igPNGyIxw6N8eRs-PloYlwbPaXg/viewform?usp=pp_url
