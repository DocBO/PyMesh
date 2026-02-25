Geometry Processing Functions
=============================

This section focuses on higher-level geometry operations (boolean, hulls,
arrangements, distance/winding queries, slicing, and subdivision).

Boolean operations
------------------

.. autofunction:: pymesh.boolean

Example (auto engine selection with runtime availability check):

.. code:: python

    import PyMesh
    import pymesh

    # Advanced engine introspection from low-level bindings.
    print(PyMesh.BooleanEngine.available_engines)
    if PyMesh.BooleanEngine.supports("igl"):
        out = pymesh.boolean(mesh_a, mesh_b, "union", engine="igl")
    else:
        out = pymesh.boolean(mesh_a, mesh_b, "union", engine="auto")

While all solid geometry operations can be done as a sequence of binary boolean
operations. It is beneficial sometimes to use :py:class:`pymesh.CSGTree` for
carrying out more complex operations.

.. autoclass:: pymesh.CSGTree
    :members:

Convex hull
-----------

.. autofunction:: pymesh.convex_hull

Example:

.. code:: python

    import pymesh
    hull = pymesh.convex_hull(mesh)

Outer hull
----------

.. autofunction:: pymesh.compute_outer_hull

Example:

.. code:: python

    import pymesh
    outer = pymesh.compute_outer_hull(mesh)

Mesh arrangement
----------------

3D arrangement:

.. autofunction:: pymesh.partition_into_cells

Example:

.. code:: python

    import pymesh
    cells = pymesh.partition_into_cells(mesh)

2D arrangement:

.. autoclass:: pymesh.Arrangement2

Minkowski sum
-------------

.. autofunction:: pymesh.minkowski_sum

Example:

.. code:: python

    import pymesh
    c = pymesh.minkowski_sum(mesh_a, mesh_b)

Subdivision
-----------

.. autofunction:: pymesh.subdivide

Example:

.. code:: python

    import pymesh
    refined = pymesh.subdivide(mesh, order=2)

Winding number query
--------------------

.. autofunction:: pymesh.compute_winding_number

Example:

.. code:: python

    import PyMesh
    import pymesh

    print(PyMesh.WindingNumberEngine.available_engines)
    wn = pymesh.compute_winding_number(mesh, query_points, engine="auto")

Slicing mesh
------------

.. autofunction:: pymesh.slice_mesh

Example:

.. code:: python

    import numpy as np
    import pymesh
    normal = np.array([0.0, 0.0, 1.0])
    slices = pymesh.slice_mesh(mesh, normal, 0.05)


Distance to mesh query
----------------------

.. autofunction:: pymesh.distance_to_mesh
.. autofunction:: pymesh.signed_distance_to_mesh
.. autofunction:: pymesh.do_intersect

Example:

.. code:: python

    import pymesh
    sq_dist, face_ids, closest_pts = pymesh.distance_to_mesh(mesh, queries)
    signed_dist, _, _ = pymesh.signed_distance_to_mesh(mesh, queries)
