Sparse Linear System Solver
===========================

Solving a sparse linear system is a common operation in geometry processing.  In
addition to the `solvers provided by scipy
<https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#solving-linear-problems>`_,
PyMesh brings the power of a number of state-of-the-art sparse solvers into
python.

Quick start (direct solver):

.. code:: python

    import numpy as np
    import scipy.sparse as sp
    import pymesh

    A = sp.diags([2.0, 2.0, 2.0], offsets=0, shape=(3, 3), format="csc")
    b = np.array([1.0, 0.0, 1.0])

    solver = pymesh.SparseSolver.create("LDLT")
    solver.compute(A)
    x = solver.solve(b)

Iterative solver with explicit tolerance/iteration control:

.. code:: python

    import pymesh

    solver = pymesh.SparseSolver.create("CG")
    solver.tolerance = 1e-10
    solver.max_iterations = 500
    solver.compute(A)
    x = solver.solve(b)

Runtime fallback across available backends:

.. code:: python

    preferred = ["PardisoLDLT", "Cholmod", "LDLT", "CG"]
    available = set(pymesh.SparseSolver.get_supported_solvers())
    solver_type = next(name for name in preferred if name in available)
    solver = pymesh.SparseSolver.create(solver_type)

Typical FE workflow (assemble then solve):

.. code:: python

    import pymesh
    from scipy.sparse.linalg import spsolve

    assembler = pymesh.Assembler(mesh, material)
    K = assembler.assemble("stiffness")
    f = ...  # external force vector

    # Option 1: PyMesh sparse solver
    solver = pymesh.SparseSolver.create("LDLT")
    solver.compute(K)
    u = solver.solve(f)

    # Option 2: SciPy solver
    u_ref = spsolve(K, f)

.. autoclass:: pymesh.SparseSolver
    :members:
