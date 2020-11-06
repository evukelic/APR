import math

"""
Constants.
"""

EPSILON = 1e-6
k = 0.5 * (math.sqrt(5)-1)
dx = 0.5
ALPHA = 1
GAMMA = 2
BETA = 0.5
SIGMA = 0.5
GOLDEN_RATIO_HEADER = '  '.join(('a', 'c', 'd', 'b', '|', 'f(a)', 'f(c)', 'f(d)', 'f(b)'))
NELDER_MEAD_HEADER = '  '.join(('xC', '|', 'f(xC)'))
HOOKE_JEEVES_HEADER = '  '.join(('xB', 'xP', 'xN', '|', 'f(xB)', 'f(xP)', 'f(xN)'))
