import PyMesh

import numpy as np

class Material:
    @classmethod
    def create(cls, density, material_tensor):
        """ Create a uniform material from the full material tensor matrix.

        Args:
            density: Material density.
            material_tensor: Flattened material tensor matrix.
                Shape must be (dim*dim, dim*dim).
        """
        return Material(PyMesh.Material.create(density, material_tensor))

    @classmethod
    def create_symmetric(cls, density, material_matrix):
        """ Create material from reduced symmetric material matrix.

        Args:
            density: Material density.
            material_matrix: Symmetric matrix in Voigt-like form.
                Shape must be 3x3 for 2D and 6x6 for 3D.
        """
        return Material(PyMesh.Material.create_symmetric(density, material_matrix))

    @classmethod
    def create_isotropic(cls, dim, density, young, poisson):
        """ Create an isotropic material.

        Args:
            dim: Dimension of the ambient space (must be 2 or 3).
            density: Material density.
            young: Young's modulus.
            poisson: Poisson's ratio
                     (must be in (-1, 0.5) in 3D and (-1, 1) in 2D).
        """
        return Material(PyMesh.Material.create_isotropic(
            dim, density, young, poisson))

    @classmethod
    def create_orthotropic(cls, density, young, poisson, shear):
        """ Create an orthotropic material.

        Args:
            desnity: Material density.
            young: Array of Young's modulus, [young_x, young_y, young_z]
            poisson: Array of Poisson's ratio, [poisson_yz, poisson_zy,
                                                poisson_zx, poisson_xz,
                                                poisson_xy, poisson_yx]
            shear: Array of Shear modulus, [shear_yz, shear_zx, shear_xy]
        """
        return Material(PyMesh.Material.create_orthotropic(
            density, young, poisson, shear))

    @classmethod
    def create_element_wise_isotropic(cls, density, mesh,
            young_attribute_name, poisson_attribute_name):
        return Material(PyMesh.Material.create_element_wise_isotropic(
            density, mesh.raw_mesh,
            young_attribute_name, poisson_attribute_name))

    @classmethod
    def create_element_wise_orthotropic(cls, density, mesh,
            young_attribute_names, poisson_attribute_names,
            shear_attribute_names):
        return Material(PyMesh.Material.create_element_wise_orthotropic(
            density, mesh.raw_mesh,
            young_attribute_names, poisson_attribute_names,
            shear_attribute_names))

    @classmethod
    def create_element_wise_symmetric(cls, density, mesh,
            matrix_attribute_name):
        return Material(PyMesh.Material.create_element_wise_symmetric(
            density, mesh.raw_mesh, matrix_attribute_name))

    @classmethod
    def create_periodic(cls, material_1, material_2, axis,
            period, ratio, phase=0.0):
        """ Create a periodic laminate material from two materials.

        Args:
            material_1: First material.
            material_2: Second material.
            axis: Lamination axis (length 2 or 3).
            period: Lamination period.
            ratio: Material ratio of material_1 in one period, in [0, 1].
            phase: Optional phase offset, in [-1, 1].
        """
        return Material(PyMesh.Material.create_periodic(
            material_1.raw_material, material_2.raw_material,
            axis, period, ratio, phase))

    def __init__(self, raw_material=None):
        self.raw_material = raw_material

    def strain_to_stress(self, strain, coord=None):
        if coord is None:
            coord = np.zeros(self.dim)
        return self.raw_material.strain_to_stress(strain, coord)

    def get_material_tensor(self, coord):
        """ Return 4th order material tensor of size d x d x d x d evaluated at
        coord.
        """
        tensor = np.empty([self.dim, self.dim, self.dim, self.dim])
        indices = np.arange(self.dim)
        I,J,K,L = np.meshgrid(indices, indices, indices, indices)
        for i,j,k,l in zip(I.ravel(), J.ravel(), K.ravel(), L.ravel()):
            tensor[i,j,k,l] = self.raw_material.get_material_tensor(
                    int(i),int(j),int(k),int(l),coord)
        return tensor

    def get_density(self, coord):
        return self.raw_material.get_density(coord)

    def update(self):
        self.raw_material.update()

    @property
    def density(self):
        """ Density at the origin.
        """
        return self.raw_material.get_density()

    @property
    def material_tensor(self):
        """ Return 4th order material tensor of size d x d x d x d evaluated at
        the origin.
        """
        coord = np.zeros(self.dim)
        return self.get_material_tensor(coord)

    @property
    def dim(self):
        """ Dimension of the ambient space.
        """
        return self.raw_material.get_dim()
