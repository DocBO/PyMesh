<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# Repository Guidelines

## Project Structure & Module Organization
- `src/`: core C++ mesh library (`PyMesh::Mesh`) and geometry/IO/attribute implementations.
- `tools/`: algorithm engines (boolean, triangulation, tetrahedralization, convex hull, etc.) consumed by the core and Python layer.
- `python/`: bindings (`python/*.cpp`) and Python package code in `python/pymesh/`.
- `tests/`: C++ unit tests (GoogleTest) plus shared test data in `tests/data/`.
- `python/pymesh/tests/`, `python/pymesh/meshutils/tests/`, `python/pymesh/wires/tests/`: Python unit tests.
- `third_party/`: submodule-based dependencies; build helpers live here.
- `docs/`: Sphinx documentation.

## Build, Test, and Development Commands
- `git submodule update --init`: fetch required third-party sources.
- `pip install -r python/requirements.txt`: install Python test/runtime deps.
- `./setup.py build`: preferred full build (third-party deps + CMake build).
- `./setup.py install --user`: local install for development.
- `python -c "import pymesh; pymesh.test()"`: run Python-facing test suite.
- `mkdir -p build && cd build && cmake .. && make -j$(nproc)`: manual CMake build.
- `cd build && make tests`: build C++ test targets.
- `cd docs && make html`: build docs locally.

## Coding Style & Naming Conventions
- C++: 4-space indentation, same-line braces, headers in `.h`, implementations in `.cpp`.
- Python: 4-space indentation, `snake_case` for functions/modules, `CamelCase` for classes, `test_*.py` for test files.
- Keep module boundaries clear: core logic in `src/`/`tools/`, lightweight API orchestration in `python/pymesh/`.
- No project-wide formatter is enforced here; follow surrounding file style closely.

## Testing Guidelines
- Add or update tests with every behavior change.
- Python tests should inherit from `pymesh.TestCase.TestCase` when helpers are useful.
- Prefer deterministic fixtures from `tests/data/` and avoid large generated artifacts in git.
- Run at minimum: `python -c "import pymesh; pymesh.test()"` before opening a PR.

## Commit & Pull Request Guidelines
- Recent history favors short, imperative commit subjects (for example: `Fix unit test failure due to json.`).
- Keep commits focused; separate refactors from behavior changes.
- PRs should include: problem statement, approach summary, impacted modules, and test evidence (commands/results).
- Link related issues and attach before/after outputs when changing CLI/scripts or mesh-processing behavior.
