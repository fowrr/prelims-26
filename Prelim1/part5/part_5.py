# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###

    
    length = len(board)
    foodLocations = []
    for j in range (0, length):
        for i in range (0, length):
            if board[j][i] == ".":
                food = (j,i)
                foodLocations.append(food)
            if board[j][i] == "x":
                platypus = (j,i)
    
    listPossibilities = []
    #def checkForFood(possible: bool, food: (int, int)):
    for foodCoordDig in range (len(foodLocations)):
        foodCoord = foodLocations[foodCoordDig]
        dist = abs(foodCoord[0] - platypus[0]) + abs(foodCoord[1] - platypus[1])
        if dist < 4:
            listPossibilities.append((foodCoord,dist))
        #if foodCoordDig == len(foodLocations):
    print(listPossibilities)
    


    #print(foodLocations)


    return final_answer
part_5(14, [
        "___.________.___",
        "________________",
        "_______________.",
        "____.__.._____..",
        "____.____.._____",
        "__.____________x",
        "__._____________",
        "__________._____",
        "________________",
        "._____._________",
        "________________",
        "____.___._______",
        "________________",
        "______________._",
        "______._________",
        "___.___.________",
    ])