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
    char_list = ["|","_", "/", " ", "\\", "."] # Making the a bank of characters
    tailB_h = size + 1 #How big my body should be in height
    tailB_l = size * 2 # this is just to fill in that big body of underscores and dots
    for x in range (0, tailB_h):   #I have 2 main for loops, which take care of the big part, and small part of the tail.
        tail_bodyLine = []  # A list that represents a line of characters, in the big body part of tail
        tail_bodyLine += char_list[0]
        for y in range (0, (tailB_l-1)):
            tail_bodyLine += char_list[1] #Here I add underscores and dots (refer to char_list)
            tail_bodyLine += char_list[5]
        tail_bodyLine += char_list[1]
        tail_bodyLine += char_list[0]
        tail_bodyLine = "".join(tail_bodyLine)
        tail.append(tail_bodyLine)
    for spaceNum in range(1,size+1):
        tail_bodyLine2 = [] # A list that represents a line of characters, in the triangle body part of tail
        for x in range(spaceNum*2):
            tail_bodyLine2 += char_list[3]
        tail_bodyLine2.insert(spaceNum, char_list[2])
        for x in range ((tailB_l) - (1 + spaceNum)):
            tail_bodyLine2.insert(spaceNum, char_list[1])
            tail_bodyLine2.insert(spaceNum, char_list[5])
        tail_bodyLine2.insert(spaceNum, char_list[1])
        tail_bodyLine2.insert(spaceNum, char_list[4])
        tail_bodyLine2 = "".join(tail_bodyLine2) # This code turns the list I am making into a string,
        tail.append(tail_bodyLine2)                  # which will then be added to my final list "tail".

    
    #test edit
    for line in tail:
        print(line, "\n")
    return tail
part_1(10)