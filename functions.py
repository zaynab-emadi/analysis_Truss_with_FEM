import math
import numpy as np


def stiffness(area, e, length, teta):
    c = math.cos(math.radians(teta))
    s = math.sin(math.radians(teta))
    keq = area * e / length * np.array([[c ** 2, c * s, -c ** 2, -c * s],
                                        [c * s, s ** 2, -c * s, -s ** 2],
                                        [-c ** 2, -c * s, c ** 2, c * s],
                                        [-c * s, -s ** 2, c * s, s ** 2]])
    return keq
