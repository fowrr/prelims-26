# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 1.
Ceci est le fichier template pour la partie 3 du Prelim 1.
"""

def part_3(sentence: str):
    """
    Find "ornithorynque" in the sentence

    Parameters:
        sentence str: The sentence that may contain contain the letters of "ornithorynque"

    Returns:
        [int]: The position of the letters found
    """
    word = "ornithorynque"
    positions = []
    ### You code goes here ###
    ### Votre code va ici ###
    letterIsChecked = False
    for letter in word:
        letterIsChecked = False
        for x in range (0, len(sentence)):
            if letterIsChecked == True:
                continue
            if letter in sentence:
                if letter == sentence[x]:
                    positions.append(x)
                    sentence = sentence[:x] + "#" + sentence[x+1:]
                    letterIsChecked = True
            elif letter not in sentence:
                positions.append(int(-1))
                letterIsChecked = True

    return positions
