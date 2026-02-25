Mesh Generation
===============

Triangulation
-------------

PyMesh supports multiple 2D triangulation backends.  The lightweight APIs
(:py:func:`pymesh.triangulate_beta` and
:py:func:`pymesh.refine_triangulation`) can auto-select the first available
engine from a preferred list at runtime.  Current triangulation candidates are:

* ``triangle_constrained_delaunay``
* ``cgal_constrained_delaunay``
* ``igl_delaunay``
* ``geogram_delaunay``
* ``jigsaw_frontal_delaunay``

For refinement, current candidates are:

* ``mmg_delaunay``
* ``triangle_refiner``

Shewchuk's `triangle library <https://www.cs.cmu.edu/~quake/triangle.html>`_
remains available via the dedicated wrapper below.

.. autoclass:: pymesh.triangle

For a lightweight API, use :py:func:`pymesh.triangulate_beta` and
:py:func:`pymesh.refine_triangulation`.

Example (triangulate with automatic backend fallback):

.. code:: python

    import numpy as np
    import PyMesh
    import pymesh

    print(PyMesh.Triangulation.available_engines)
    pts = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    seg = np.array([[0, 1], [1, 2], [2, 0]])
    mesh = pymesh.triangulate_beta(pts, seg, engine="auto")

Tetrahedralization
------------------

In contrast with 2D, tetrahedralization in 3D is a much harder problem.  Many
algorithms try to tackle this problem from different angles.  No single
algorithm or package stands out as the best.  We therefore offer a number of
different engines for our users.

.. autofunction:: pymesh.tetrahedralize

Example (tetrahedralize with automatic backend fallback):

.. code:: python

    import PyMesh
    import pymesh

    print(PyMesh.TetrahedralizationEngine.available_engines)
    tet_mesh = pymesh.tetrahedralize(surface_mesh, cell_size=0.05, engine="auto")

In addition to :py:func:`pymesh.tetraheralize`, we also provide a more complete
wrapper around Si's awesome `TetGen <http://wias-berlin.de/software/tetgen/>`_
package.

.. autoclass:: pymesh.tetgen
