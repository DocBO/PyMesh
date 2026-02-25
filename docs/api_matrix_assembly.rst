Finite Element Matrix Assembly
==============================

PyMesh exposes finite element assembly through ``pymesh.Assembler`` and
material models through ``pymesh.Material``.

Common matrices supported by ``Assembler.assemble(name)``:

* ``stiffness``
* ``mass``
* ``lumped_mass``
* ``laplacian``
* ``displacement_strain``
* ``elasticity_tensor``
* ``engineer_strain_stress``
* ``rigid_motion``
* ``gradient``
* ``graph_laplacian``

Use ``Material`` factories to define constitutive behavior:

* ``create`` for a full material tensor matrix.
* ``create_symmetric`` for reduced symmetric material matrices (Voigt-like).
* ``create_isotropic`` and ``create_orthotropic`` for standard solids.
* ``create_periodic`` for layered/laminated periodic media.
* ``create_element_wise_*`` variants for per-element material parameters.

Quick example:

.. code:: python

    import numpy as np
    import pymesh

    mesh = pymesh.generate_box_mesh(
        np.array([0.0, 0.0, 0.0]),
        np.array([1.0, 1.0, 1.0]),
        num_samples=2)

    mat = pymesh.Material.create_isotropic(
        dim=3, density=1.0, young=1.0e5, poisson=0.3)
    assembler = pymesh.Assembler(mesh, mat)

    K = assembler.assemble("stiffness")
    M = assembler.assemble("mass")

Construct material from a symmetric matrix (recently exposed in Python API):

.. code:: python

    import numpy as np
    import pymesh

    # 2D symmetric material matrix: [xx, yy, xy] x [xx, yy, xy]
    C = np.array([
        [2.0, 0.5, 0.0],
        [0.5, 2.0, 0.0],
        [0.0, 0.0, 0.8],
    ])
    mat = pymesh.Material.create_symmetric(density=1.0, material_matrix=C)

Periodic laminate material (recently exposed in Python API):

.. code:: python

    import numpy as np
    import pymesh

    mat_1 = pymesh.Material.create_isotropic(2, density=1.0, young=1000.0, poisson=0.25)
    mat_2 = pymesh.Material.create_isotropic(2, density=2.0, young=2000.0, poisson=0.25)
    laminate = pymesh.Material.create_periodic(
        mat_1, mat_2, axis=np.array([1.0, 0.0]), period=2.0, ratio=0.5, phase=0.0)

Element-wise materials from mesh attributes (recently exposed in Python API):

.. code:: python

    import pymesh

    # mesh should contain per-element attributes with these names.
    ew_ortho = pymesh.Material.create_element_wise_orthotropic(
        density=1.0,
        mesh=mesh,
        young_attribute_names=["young_x", "young_y", "young_z"],
        poisson_attribute_names=[
            "poisson_yz", "poisson_zy", "poisson_zx",
            "poisson_xz", "poisson_xy", "poisson_yx"],
        shear_attribute_names=["shear_yz", "shear_zx", "shear_xy"])

    ew_sym = pymesh.Material.create_element_wise_symmetric(
        density=1.0,
        mesh=mesh,
        matrix_attribute_name="material_matrix")

.. autoclass:: pymesh.Assembler
    :members:

.. autoclass:: pymesh.Material
    :members:
