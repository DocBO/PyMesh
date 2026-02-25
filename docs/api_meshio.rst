Reading and Writing Meshes
==========================

Use these functions to load/save mesh files and to construct in-memory meshes
from NumPy arrays.

Example:

.. code:: python

    import numpy as np
    import pymesh

    # Load from disk.
    mesh = pymesh.load_mesh("input.obj")

    # Build mesh from arrays.
    V = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    F = np.array([[0, 1, 2]])
    tri = pymesh.form_mesh(V, F)

    # Save with attributes.
    tri.add_attribute("face_area")
    pymesh.save_mesh("output.obj", tri, "face_area")

.. autofunction:: pymesh.meshio.load_mesh

.. autofunction:: pymesh.meshio.save_mesh

.. autofunction:: pymesh.meshio.save_mesh_raw

.. autofunction:: pymesh.meshio.form_mesh
