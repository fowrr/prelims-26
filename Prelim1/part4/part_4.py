# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""

def part_4(positions: [(int, int, int)]):
    """
    Find the closest preys to the platypus

    Parameters:
        positions [(int, int, int)]: The position of the platypus and all the preys

    Returns:
        [int]: The ascending order of the preys' distance to the platypus
    """
    order = []
    ### You code goes here ###
    ### Votre code va ici ###
    import math
    print(positions)
    preOrder = []
    distList = []
    initPos = positions[0]
    distances = len(positions)
    for preyDis in range (1,distances):
        prey = positions[preyDis]
        dist = math.sqrt( ((initPos[0]-prey[0])**2) + ((initPos[1]-prey[1])**2) + ((initPos[2]-prey[2])**2) )
        distTuple = (preyDis, dist)
        distList.append(dist)
        preOrder.append(distTuple)
    distList.sort()
    for ordDist in distList:
        for y in range (0,len(preOrder)):
            ordDistTuple = preOrder[y]
            if ordDist == ordDistTuple[1]:
                order.append(ordDistTuple[0])
        
    print(order)
    return order

part_4([(0,0,0),(5,3,9), (1,2,25),(11, 16, 14), (8, 4, 9), (11, 18, 8), (17, 2, 15),(4, 13, 6), (2, 6, 4), (3, 1, 7)])