Procedural Mesh Generation
==========================

These helpers create canonical meshes directly from parameters.

Example:

.. code:: python

    import numpy as np
    import pymesh

    box = pymesh.generate_box_mesh(
        np.array([0.0, 0.0, 0.0]),
        np.array([1.0, 1.0, 1.0]),
        num_samples=2)
    sphere = pymesh.generate_icosphere(1.0, np.zeros(3), refinement_order=2)

Equilateral triangle generation
-------------------------------

.. autofunction:: pymesh.generate_equilateral_triangle

Box generation
--------------

.. autofunction:: pymesh.generate_box_mesh

Sphere generation
-----------------

.. autofunction:: pymesh.generate_icosphere

Cylinder generation
-------------------

.. autofunction:: pymesh.generate_cylinder

Tube generation
-------------------

.. autofunction:: pymesh.generate_tube


Other Platonic solids
---------------------

.. autofunction:: pymesh.generate_regular_tetrahedron
.. autofunction:: pymesh.generate_dodecahedron

Wire mesh generation
--------------------

.. autoclass:: pymesh.wires.WireNetwork
    :members:

.. autoclass:: pymesh.wires.Parameters
    :members:

.. autoclass:: pymesh.wires.Tiler
    :members:

.. autoclass:: pymesh.wires.Inflator
    :members:
