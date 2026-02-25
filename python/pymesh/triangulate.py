import PyMesh
from .meshio import form_mesh
import numpy as np
from time import time

def triangulate_beta(points, segments, engine="auto", with_timing=False):
    """ Triangulate 2D points/segments into a triangle mesh.

    Args:
        points (:class:`numpy.ndarray`): Input points of shape N by 2.
        segments (:class:`numpy.ndarray`): Segment indices of shape M by 2.
        engine (``string``): Triangulation engine name.

            * ``auto``: choose first available engine from
              ``triangle_constrained_delaunay``,
              ``cgal_constrained_delaunay``, ``igl_delaunay``,
              ``geogram_delaunay``, ``jigsaw_frontal_delaunay``.
        with_timing (``boolean``): Whether to return running time.

    Returns:
        Triangulated mesh, or ``(mesh, running_time)`` if ``with_timing``.

    Engine availability can be queried through low-level bindings using
    ``PyMesh.Triangulation.supports(name)`` and
    ``PyMesh.Triangulation.available_engines``.
    """
    if engine == "auto":
        preferred = [
            "triangle_constrained_delaunay",
            "cgal_constrained_delaunay",
            "igl_delaunay",
            "geogram_delaunay",
            "jigsaw_frontal_delaunay",
        ]
        for name in preferred:
            if PyMesh.Triangulation.supports(name):
                engine = name
                break
        else:
            raise NotImplementedError("No supported triangulation engine")

    engine = PyMesh.Triangulation.create(engine)
    engine.set_points(points)
    engine.set_segments(segments)

    if with_timing:
        start_time = time()

    engine.run()

    if with_timing:
        finish_time = time()
        running_time = finish_time - start_time

    vertices = engine.get_vertices()
    faces = engine.get_faces()

    mesh = form_mesh(vertices, faces)
    if with_timing:
        return mesh, running_time
    else:
        return mesh


def refine_triangulation(mesh, metrics=None, engine="auto", with_timing=False):
    """ Refine an existing triangle mesh.

    Args:
        mesh (:class:`Mesh`): Input triangle mesh.
        metrics (:class:`numpy.ndarray`): Optional per-vertex sizing field.
        engine (``string``): Refinement engine name.

            * ``auto``: choose first available engine from
              ``mmg_delaunay`` and ``triangle_refiner``.
        with_timing (``boolean``): Whether to return running time.

    Returns:
        Refined mesh, or ``(mesh, running_time)`` if ``with_timing``.
    """
    if engine == "auto":
        preferred = ["mmg_delaunay", "triangle_refiner"]
        for name in preferred:
            if PyMesh.Triangulation.supports(name):
                engine = name
                break
        else:
            raise NotImplementedError("No supported refinement engine")

    engine = PyMesh.Triangulation.create(engine)
    engine.set_vertices(mesh.vertices)
    engine.set_faces(mesh.faces)

    if with_timing:
        start_time = time()

    if metrics is None:
        engine.refine(np.zeros((0,1)))
    else:
        engine.refine(metrics)

    if with_timing:
        finish_time = time()
        running_time = finish_time - start_time

    vertices = engine.get_vertices()
    faces = engine.get_faces()

    mesh = form_mesh(vertices, faces)
    if with_timing:
        return mesh, running_time
    else:
        return mesh
