#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
from polyproject import polyproject


def test_diamond():
    a = np.array([[2, 1],
                  [1, 2],
                  [2, 3],
                  [3, 2]])
    point = np.array([0, 0])

    from scipy.spatial import ConvexHull
    c = ConvexHull(a)
    x, _ = polyproject(point, polyhedron=c.equations)

    assert np.allclose(x, np.array([1.5, 1.5]))


def test_square():
    a = np.array([[1, 1],
                  [1, 2],
                  [2, 1],
                  [2, 2]])
    point = np.array([0, 0])

    x, _ = polyproject(point, vertices=a)

    assert np.allclose(x, np.array([1, 1]))


def test_value_error():
    import pytest

    point = np.array([0, 0])

    with pytest.raises(ValueError, message='Expecting ValueError'):
        polyproject(point)


#def test_plot():
#    import matplotlib.pyplot as plt
#    a = np.array([[2, 1],
#                  [1, 2],
#                  [2, 3],
#                  [3, 2]])
#    point = np.array([0, 0])
#
#    from scipy.spatial import ConvexHull, convex_hull_plot_2d
#    c = ConvexHull(a)
#
#    x, _ = polyproject(point, polyhedron=c.equations)
#
#    convex_hull_plot_2d(c, plt.gca())
#    plt.plot([point[0], x[0]], [point[1], x[1]], 'C1x-')
#
#    # TODO: What do we assert?
