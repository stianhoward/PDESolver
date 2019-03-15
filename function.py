
def func(center, left, right, top, bottom):
    return quarter(center, left, right, top, bottom)

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

def test(center, left, right, top, bottom):
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

    return centerVal + (topVal + bottomVal + leftVal + rightVal - 4 * centerVal) * 0.5





# Now to try the equation for the quarter circle

# (100) (100)
# |
# |  1   2   3   (100)
# |
# |  4   5   6   7   (100)
# |
# |  8   9   10  11  12  (100)
# |
# |  13  14  15  16  17  (100)
# |_______________________
#    (0) (0) (0) (0) (0)
#

def quarter(center, left, right, top, bottom):
    # Conditions for the edges being None
    # Left
    if left == None:
        leftVal = right.T
        leftDist = 0.2
    else:
        leftVal = left.T
        leftDist = abs(center.dist['left'])
    
    # Right
    if right == None:
        rightVal = 100
        # Determine what the right level is
        if (center.x == 0.4 or center.x == 0.6):
            rightDist = 0.2
        elif center.x  == 0.8:
            if center.y == 0.2:
                rightDist = 0.899 * 0.2
            else:
                rightDist = 0.5826 * 0.2
    else:
        rightVal = right.T
        rightDist = abs(center.dist['right'])
    
    # Top
    if top == None:
        topVal = 100
        # Determine the top distance
        if (center.y == 0.4 or center.y == 0.6):
            topDist = 0.2
        elif center.y  == 0.8:
            if center.x == 0.2:
                topDist = 0.899 * 0.2
            else:
                topDist = 0.5826 * 0.2
    else:
        topVal = top.T
        topDist = abs(center.dist['top'])
    
    # Bottom
    if bottom == None:
        bottomVal = 0
        bottomDist = 0.2
    else:
        bottomVal = bottom.T
        bottomDist = center.dist['bottom']
    
    # Center
    centerVal = center.T

    distSum = leftDist + rightDist
    dx = ( (leftVal / (leftDist * distSum)) - (centerVal / (leftDist * rightDist)) + (rightVal / (rightDist * distSum)) )
    distSum = bottomDist + topDist
    dy = ( (bottomVal / (bottomDist * distSum)) - (centerVal / (bottomDist * topDist)) + (topVal / (topDist * distSum)) )
    #Randomly multiplying by 0.001 in order to prevent diverging solution...
    return centerVal + (dx + dy) * 0.001