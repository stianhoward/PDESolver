# TODO:
# - Create a method for printing/ showing the results of the simulation
# BUG: Bug in the solve function. Not resulting in the correct results. Think error is in function.py


from initialize import initialize
from solving import solve

def main():
    # Initialize the data network to be the correct size/ shape
    nodes = initialize('quarterCircle.csv')

    # Run through the actual simulation stuff
    results = solve(nodes, 1.0e-6)

    # Display the results
    for node in results:
        printNode(node)

def printNode(node):
    print("x, y, T: ", node.x, node.y, node.T)


if __name__ == "__main__":
    main()