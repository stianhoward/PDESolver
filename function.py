# This is the equation that is used to actually solve stuff in this situation


#       4 4 4 4  
#   \| ---------|\
#   \| 1   2   3|\
#   \|          |\
#   \| 4   5   6|\
#   \|          |\
#   \| 7   8   9|\
#   \|----------|\
#     2  2  2  2
# Equations for the setup with insulation on the left and right, and T=4 on the top, and T=2 on the bottom

def func(center, left, right, top, bottom):
    # Be aware that many of these may be 'None'. Account for that in here.
    # This will largely have to do with the boundary conditions of the system.
    # There will be 8 conditions I think.... Although this depends on how this is written

    # Conditions for the edges being None
    if left == None:
        leftVal = right.T
    else:
        leftVal = left.T
    if right == None:
        rightVal = left.T
    else:
        rightVal = right.T
    if top == None:
        topVal = 4
    else:
        topVal = top.T
    if bottom == None:
        bottomVal = 2
    else:
        bottomVal = bottom.T
    centerVal = center.T

    return (topVal + bottomVal + leftVal + rightVal - 4 * centerVal)*0.04