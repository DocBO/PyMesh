Mesh Data Structure
===================

``pymesh.Mesh`` stores geometry and topology:

* ``vertices``: ``N x dim`` floating-point array.
* ``faces``: ``F x 3`` integer array for triangle surfaces.
* ``voxels``: ``T x 4`` integer array for tetrahedral volume meshes.

Typical workflow:

.. code:: python

    import pymesh
    mesh = pymesh.load_mesh("input.obj")

    # Query dimensions/topology
    print(mesh.dim, mesh.num_vertices, mesh.num_faces, mesh.num_voxels)

    # Compute and read attributes
    mesh.add_attribute("face_area")
    area = mesh.get_attribute("face_area")

    # Access raw arrays
    V = mesh.vertices
    F = mesh.faces

.. autoclass:: pymesh.Mesh
    :members:
