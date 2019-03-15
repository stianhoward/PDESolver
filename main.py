# TODO:
# - Create a method for printing/ showing the results of the simulation

from initialize import initialize
from solving import solve

''' --------------------------
# Default setups. Uncomment 'networkfile' as appropriate and adjust function call from func() in function.py
---------------------------'''

# Polar solution: Change func() in function.py to call polarCircle()
networkfile = 'networks/polarCircle.csv'
# Cartesian solution: Change func() in function.py to call cartesianCircle()
#networkfile = 'networks/cartesianCircle.csv'


def main():
    # Initialize the data network to be the correct size/ shape
    nodes = initialize(networkfile)

    # Run through the actual simulation stuff
    results = solve(nodes, 1.0e-6)

    # Display the results
    for node in results:
        printNode(node)

def printNode(node):
    print("x, y, T: ", node.x, node.y, node.T)


if __name__ == "__main__":
    main()