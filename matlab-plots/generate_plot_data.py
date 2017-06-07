#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
from polyproject import polyproject
from scipy.spatial import ConvexHull
from scipy import io


if __name__ == '__main__':
    a = np.random.rand(25, 3)
    point = np.array([0, 0, 0])

    c = ConvexHull(a)
    x, _ = polyproject(point, polyhedron=c.equations)

    io.savemat('plot_data.mat', {'vertices': c.points, 'faces': c.simplices,
                                 'point': point, 'projected_point': x})
