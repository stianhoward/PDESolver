import math

class Node:
    # Initialize the node to a certain position
    def __init__(self, x, y, area):
        self.x = x
        self.y = y
        self.T = 1
        self.area = area
        self.neighbours = {
            "left": None,
            "right": None,
            "top": None,
            "bottom": None
        }
        self.dist = {
            "left": None,
            "right": None,
            "top": None,
            "bottom": None
        }
    
    # Add a reference to a neighbour
    def addNeighbour(self, nodes, array):
        for node in nodes:
            self.neighbours[node[1]] = array[node[0] - 1]
            self.dist[node[1]] = self.calcDist(array[node[0] - 1])
        # update the area of the point. Not sure if this is actually gonig ot be applicable

    def calcDist(self, otherNode):
        dx = self.x - otherNode.x
        dy = self.y - otherNode.y
        dist = math.sqrt(dx**2 + dy**2)
        return dist