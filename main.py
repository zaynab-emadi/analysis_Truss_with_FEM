import numpy as np


# nodal matrix statically
# it should be a matrix with size of NoN(numbers of nodes) * PD(problem dimension)
nodesMatrix = np.array([[0, 0],
                        [1, 0],
                        [0.5, 1]])
# matrix of elements
# it should be a matrix with size of NoE(number of elements) * NPE(nodes per element)
elementsMatrix = np.array([[1, 2],
                           [2, 3],
                           [3, 1]])
# add boundary condition
boundaryCondition = np.array([-1, -1],
                             [1, -1],
                             [1, 1])
