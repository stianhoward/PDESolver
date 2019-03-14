# PDESolver

An oversimplified PDESolver built in python for Intermediate Numerical Analysis 2  class.

## Getting Started

- Clone the code to your computer in a working directory
    - Alternatively download a zip of the code if you don't want updates to the code or be able to easily push your updates
- Alter the *function.py* and file import (default *Book1.csv*) to represent your environment
    - *function.py* is the actual PDE to be solved. At the moment it also contains conditions for the boundary conditions
    - *Book1.csv* contains the nodes and relations between the nodes in your desired environment. It is always input as 'x_position, y_position, area, relations', where relations is written as 'node_#, position' is the relations.
        - First line of the CSV is not read
        - An example of input is '0,0,0.04,2,right,4,top
        - In this example, we input a node with position (0,0) with area 0.04. Node 2 is the right neighbour, and node 4 is the top neighbour
- Run the code
```
python ./main.py
```

### Prerequisites

The code was developed with python 3.7. I have no idea if it is backwards compatible.
