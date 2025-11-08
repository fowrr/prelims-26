# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: [str]):
    for line in tail:
        print(line)

def part_1(size: int):
    """
    Draw the platypus tail

    Parameters:
        size int: Size of the tail

    Returns:
        [String]: The platypus tail drawn
    """
    tail = []
    ### YOUR CODE GOES HERE ###
    print(size)
    char_list = ["|","_", "/", " ", "\\", "."] 
    tailB_h = size + 1
    tailB_l = size * 2
    for x in range (0, tailB_h):
        tail_bodyLine = []
        tail_bodyLine += char_list[0]
        for y in range (0, (tailB_l-1)):
            tail_bodyLine += char_list[1]
            tail_bodyLine += char_list[5]
        tail_bodyLine += char_list[1]
        tail_bodyLine += char_list[0]
        tail.append(tail_bodyLine)
    for spaceNum in range(1,size+1):
        tail_bodyLine2 = []
        for x in range(spaceNum):
            print()
        print(spaceNum)
    for line in tail:
        print(*line, "\n")
    #test edit

    return tail
part_1(2)
