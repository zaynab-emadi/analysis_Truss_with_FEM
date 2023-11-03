import numpy as np


# nodal matrix statically
# it should be a matrix with size of NoN(numbers of nodes) * PD(problem dimension)
nodesList = np.array([[0, 0],
                      [1, 0],
                      [0.5, 1]])
# matrix of elements
# it should be a matrix with size of NoE(number of elements) * NPE(nodes per element)
elementsList = np.array([[1, 2],
                         [2, 3],
                         [3, 1]])
# add boundary condition
boundaryCondition = np.array([[-1, -1],
                             [1, -1],
                             [1, 1]])
# add forces
Forces = np.array([[0, 0],
                   [0, 0],
                   [0, -20]])
# displacement
displacement = np.array([[0, 0],
                         [0, 0],
                         [0, 0]])
# define the young's modulus
E = 10 ** 6
# define cross-section area
A = 0.01
# define problem dimension which is number of columns in nodeLists
PD = np.size(nodesList, 1)
# define number of nodes which is number of rows in nodesList
NoN = np.size(nodesList, 0)
# define extended node list with full of zeros which will be the size of NoN * 6PD
extendedNodeList = np.zeros([NoN, 6*PD])
# assign node lists to enl
extendedNodeList[:, 0:PD] = nodesList[:, :]
# assign boundary condition to enl
extendedNodeList[:, PD:2*PD] = boundaryCondition[:, :]
print(extendedNodeList)