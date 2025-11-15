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
                food = (i,j)
                foodLocations.append(food)
            if board[j][i] == "x":
                platypus = (i,j)
  
   #We have gotten all the foods and the platypus' position


   #checks closest food (to optimize code, so we will not have to check through foodLocations every single time)
    def checkCloseFoods():
        closeFoods = []
        for x in range (len(foodLocations)):
            food = foodLocations[x]
            dist = abs(food[0]-platypus[0]) + abs(food[1]-platypus[1])
            if dist < 4:
                closeFoods.append(food)
        return closeFoods


   #priority ---> right, down, left, up


  
    while turns > 0:
        relativeFoods = checkCloseFoods()  #So now we will check for foods located on the vertical/horizontal axis relative to the platypus
        importance = [[],[],[],[]] #4 lists : for the ones in the right
        for x in range (len(relativeFoods)):
            food = relativeFoods[x]
            if food[0] != platypus[0] and platypus[1] != food[1]:
                pass
            else:
                if food[0] - platypus[0] > 0: #food is right of platypus
                    axisFood = (food, food[0] - platypus[0])
                    importance[0].append(axisFood)
                if food[1] - platypus[1] > 0: #food is below of platypus
                    axisFood = (food, food[1] - platypus[1])
                    importance[1].append(axisFood)
                if platypus[0] - food[0] > 0: #food is left of platypus
                    axisFood = (food, platypus[0] - food[0])
                    importance[2].append(axisFood)
                if platypus[1] - food[1] > 0: #food is above of platypus
                    axisFood = (food, platypus[1] - food[1])
                    importance[3].append(axisFood)
        for lists in importance:
            sorted(lists, key=lambda x: x[1])
        print(importance)
        turns = -1

    
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