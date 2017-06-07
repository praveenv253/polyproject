#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import cvxpy as cvx


def polyproject(point, polyhedron=None, vertices=None):
    """
    Projects a point onto a convex polyhedron. Makes use of cvxpy.

    The polyhedron can be specified either as a set of vertices, or as a matrix
    of equations describing the polyhedron. In the former case, the convex hull
    of the vertices is computed. In the latter case, the input is a matrix `A`
    such that A * [x, y, z]^T = [0, 0, 0]^T (in 3D).

    Parameters
    ----------
    point : array of shape (ndim,)
        Point to project onto the polyhedron
    polyhedron : array of shape (nfacets, ndim+1), optional
        Array containing the matrix of equations describing the polyhedron.
        Either this option or `vertices` must be provided.
    vertices : array of shape (nvertices, ndim), optional
        Array containing the vertices of the polyhedron. Either this parameter
        or `polyhedron` must be provided. Ignored if polyhedron is provided.

    Returns
    -------
    proj_point : array of shape (ndim,)
        Projection of the given point onto the convex polyhedron.
    polyhedron : array of shape (nfacets, ndim+1), optional
        Array containing the matrix of equations describing the polyhedron.

    Raises
    ------
    ValueError
        If neither `vertices` nor `polyhedron` is provided.
    """

    if polyhedron is None:
        if vertices is None:
            raise ValueError('Must provide either vertices or polyhedron.')
        from scipy.spatial import ConvexHull
        conv_hull = ConvexHull(vertices)
        polyhedron = conv_hull.equations

    # Set up the convex optimization problem
    ndim = point.size
    x = cvx.Variable(ndim)
    objective = cvx.Minimize(cvx.sum_entries(cvx.square(x - point)))
    constraints = [polyhedron[:, :-1] * x <= -polyhedron[:, -1],]
    prob = cvx.Problem(objective, constraints)

    final_obj = prob.solve()
    #print(final_obj)
    #print(x.value)

    return np.array(x.value), polyhedron
