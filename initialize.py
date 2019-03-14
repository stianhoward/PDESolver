from objects.nodes import Node
import csv

def initialize(fileName = None):
    # Import the data
    if fileName != None:
        input = importNodes(fileName)
    else:
        # Temporary list of objects for the program to add as nodes
        input = [[1,2,4,[[2,"top"],[3,"right"]]],[1,3,4,[[1,"bottom"]]],[2,2,4,[[1,"left"]]],[5,6,4,[]]]
    

    # Create an empty array to add the objects to and add objects
    nodes = []

    # Add all nodes to the list of nodes
    for item in input:
        nodes.append(Node(item[0],item[1],item[2]))

    # Now do the loop again but add neighbours as needed
    for k in range(len(nodes)):
        #just some stuff
        nodes[k].addNeighbour(input[k][3], nodes)
    
    return nodes

def importNodes(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader,None)
        nodes = []
        for row in reader:
            relations = row[3:]
            neighbours = []
            for k in range(int(len(relations)/2)):
                neighbours.append([int(relations[2*k]), relations[2*k+1]])

            nodes.append([float(row[0]), float(row[1]), float(row[2]), neighbours])

    return nodes

if __name__ == "__main__":
    initialize()