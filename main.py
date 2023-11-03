import numpy as np
import math
from functions import stiffness

# nodal matrix statically
# it should be a matrix with size of NoN(numbers of nodes) * PD(problem dimension)
# label of node will be its index+1
nodesList = np.array([[0, 0],
                      [1, 2],
                      [2, 0],
                      [3, 2],
                      [4, 0],
                      [5, 2],
                      [6, 0],
                      [7, 2],
                      [8, 0]])

# matrix of elements
# it should be a matrix with size of NoE(number of elements) * NPE(nodes per element)
# label of element will be its index+1
elementsList = np.array([[1, 2],
                         [1, 3],
                         [2, 3],
                         [2, 4],
                         [4, 3],
                         [3, 5],
                         [4, 5],
                         [4, 6],
                         [6, 5],
                         [5, 7],
                         [6, 7],
                         [6, 8],
                         [7, 8],
                         [7, 9],
                         [8, 9]])

# define number of nodes which is number of rows in nodesList
# axis 0 shows number of rows and axis 1 shows number of columns
NoN = np.size(nodesList, 0)

# define number of elements which is number of rows in elementsLists
NoE = np.size(elementsList, 0)

# define cross-section area
# size of this matrix should be NoE * 1
area = np.ones([NoE, 1])

# in this problem we have different area for horizontal and diagonal members
for i in range(0, NoE):
    if i % 2 == 0:
        area[i] = 0.02
    else:
        area[i] = 0.045


# define young's module
E = 30*10**9*np.ones([NoE, 1])

# initial length and angle matrices
L = np.zeros([NoE, 1])
angle = np.zeros([NoE, 1])

# calculating the length and angle of each element
for i in range(0, NoE):
    [element] = elementsList[i:i+1]
    # finding label of nodes
    node1 = element[0]
    node2 = element[1]
    xNode1 = nodesList[node1-1, 0]
    xNode2 = nodesList[node2-1, 0]
    yNode1 = nodesList[node1-1, 1]
    yNode2 = nodesList[node2-1, 1]
    elementLen = math.sqrt(pow(xNode1-xNode2, 2)+pow(yNode1-yNode2, 2))
    elementAng = math.degrees(math.atan((yNode2-yNode1)/(xNode2-xNode1)))
    if elementAng < 0:
        elementAng = 180 + elementAng
    angle[i] = elementAng
    L[i] = elementLen

print(stiffness(0.2, 30*10**9, 2, 45))
