import PyMesh

def compute_winding_number(mesh, queries, engine="auto"):
    """ Compute winding number with respect to `mesh` at `queries`.

    Args:
        mesh (:class:`Mesh`): The mesh for which winding number is evaluated.
        queries (:class:`numpy.ndarray`): N by 3 matrix of query points at which
            winding number is evaluated.
        engine (``string``): (optional) Winding number computing engine name:

            * ``auto``: use first available engine from
              ``igl`` and ``fast_winding_number``.
            * ``igl``: use libigl's `generalized winding number`_.
            * ``fast_winding_number``: use code from `fast winding number`_
              paper. It is faster than ``igl`` but can be less accurate sometimes.


    Returns:
        A list of size N, represent the winding numbers at each query points in
        order.

    .. _`generalized winding number`: https://libigl.github.io/tutorial/#generalized-winding-number
    .. _`fast winding number`: http://www.dgp.toronto.edu/projects/fast-winding-numbers/

    Engine availability can be queried from low-level bindings via
    ``PyMesh.WindingNumberEngine.supports(name)`` and
    ``PyMesh.WindingNumberEngine.available_engines``.
    """
    assert(mesh.dim == 3)
    assert(mesh.vertex_per_face == 3)

    if engine == "auto":
        preferred = ["igl", "fast_winding_number"]
        for name in preferred:
            if PyMesh.WindingNumberEngine.supports(name):
                engine = name
                break
        else:
            raise NotImplementedError("No supported winding number engine")

    engine = PyMesh.WindingNumberEngine.create(engine)
    engine.set_mesh(mesh.vertices, mesh.faces)
    winding_numbers = engine.run(queries).ravel()

    return winding_numbers
