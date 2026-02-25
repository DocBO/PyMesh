## Why
The repository still documents and configures Python 2.7 support, which is obsolete and conflicts with the requested modern baseline. This causes misleading setup instructions and unnecessary compatibility surface.

## What Changes
- Remove Python 2.7 references from contributor/user documentation.
- Set and document project Python support baseline to Python 3.13+.
- Remove legacy Python 2 CI jobs and related Docker workflow references.
- Remove Python 2 compatibility fallback code in the Python package initialization.

## Impact
- Affected specs: `python-runtime-support`
- Affected code/docs:
  - `README.md`
  - `docs/installation.rst`
  - `.travis.yml`
  - `.circleci/config.yml`
  - `docker/patches/extract_wheel.sh`
  - `docker/py2.7/` and `docker/py2.7-slim/` (removed)
  - `python/pymesh/__init__.py`
