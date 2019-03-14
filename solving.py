# Set of function to solve the PDE for a result until we meet the tolerance at all points

from function import func

def solve(nodes, tol):
    # initialize madDel as greater than the tolerance
    madDel = tol + 1
    iterator = 0
    while (madDel > tol) and iterator < 1000:
        newValues = []
        iterator = iterator + 1
        print(iterator)

        # Iterate through the nodes and solve as needed
        for k in range(len(nodes)):
            node = nodes[k]
            val = func(node,node.neighbours["left"],node.neighbours["right"],node.neighbours["top"],node.neighbours["bottom"])
            newValues.append(val)
        #some equation

        # Calculate the max change, 'madDel', of the new positions
        madDel = calcDel(newValues, nodes)
        for k in range(len(newValues)):
            nodes[k].T = newValues[k]

    return nodes

def calcDel(newValues, nodes):
    maxDel = 0
    for k in range(len(newValues)):
        change = abs(newValues[k] - nodes[k].T)
        if change > maxDel:
            maxDel = change
    return maxDel