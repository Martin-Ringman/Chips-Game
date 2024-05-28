# This program lets a human play against the computer in the game of chips  
# It uses 5 different functions all called by a main program to achieve the goal of taking user input
# for how many chips the game should have, displaying a version of the chip piles, getting the user
# input for which pile they would like to take from and how many chips from the given pile, updating
# the amount of chips in each pile, and deciding what the computers move is. These tasks are broken
# up into their own function for clarity and to use less code since the functions can be called multiple
# times.
# The main part of the program brings everything together by calling indiviual functions, assinging some
# global variables to get data between functions, using print to update the user on the status of the
# game, and deciding if the game is over along with letting the user know this. 

import time
import doctest

########################
# 
def initializeGame():
    """
    void -> int
    PRE:  Nothing is passed to this function
    POST: A valid number of chips is returned
    """
    
    chips = 0
    while chips <= 0:
        chips = int(input("How many chips to start with in each pile? "))
        if chips <= 0:
            print("Sorry you can't start with zero or fewer chips!")
            print("Try again.")
        
    return chips
 
# Since this function has no input from outside the function it doesn't make sense to use doctest
# to figure out if it is working correctly. I tested this function by commenting out pretty much all
# of the main program temporarily, leaving only the call to initializeGame, and adding a temporary
# print function to make sure that the users choice for how many chips to start with was successfully
# stored in the local variable, and returned to the main function, able to be printed and verified.
#
# end of initializeGame
#######################



#######################
#
def displayPiles(pile1, pile2):
    """
    int,int -> void
    PRE:  Two non-negative integers are passed to the function
    POST: The piles of chips are displayed to the screen where each
          chip is an "O".  A space inserted after every fifth chip to
          improve readability. Further, a newline is inserted after
          both piles are displayed
    >>> displayPiles(3,6)
    Pile 1: OOO
    Pile 2: OOOOO O
    <BLANKLINE>
    >>> displayPiles(6,4)
    Pile 1: OOOOO O
    Pile 2: OOOO
    <BLANKLINE>
    >>> displayPiles(1,6)
    Pile 1: O
    Pile 2: OOOOO O
    <BLANKLINE>
    >>> displayPiles(7,7)
    Pile 1: OOOOO OO
    Pile 2: OOOOO OO
    <BLANKLINE>
    """
    currentPile1 = pile1
    currentPile2 = pile2
    spaceCheck1 = 1 
    spaceCheck2 = 1
    
    print("Pile 1: ", sep = "", end = "")
    while currentPile1 > 0:
        print("O", sep = "", end = "")
        if spaceCheck1 % 5 == 0:
            print(" ", sep = "", end = "")
        currentPile1 -= 1
        spaceCheck1 += 1
    
    print("\nPile 2: ", sep = "", end = "")
    while currentPile2 > 0:
        print("O", sep = "", end = "")
        if spaceCheck2  % 5 == 0:
            print(" ", sep = "", end = "")
        currentPile2 -= 1
        spaceCheck2 += 1
    print("\n")
#
# end of displayPiles ###########

#########################
#
def getHumanMove(p1chips, p2chips):
    """
    int,int -> int,int
    PRE:  Two integers, both non-negative, at least one larger than zero, are passed in.  The
          first number represents the count of chips in pile 1, the second number is the count of
          chips in pile 2
    POST: Two values are returned: (1) the pile that the human player has chosen (e.g. 1 or 2)
          which I'll call humanPile. (2)the number of chips that the human would like to take
          from his chosen pile which I'll call humanChips.  The function ensures that the move is
          valid but does not update the number of chips in either pile.
          To be precise, upon returning the function ensures that there are at least
          humanChips chips left in humanPile   
    """
    pileChoice = 0
    chipChoice = -1
    
    while (pileChoice != 1 and pileChoice != 2) or chipChoice > p1chips or chipChoice <= 0 :
        pileChoice = int(input("Which pile would you like to take from? (1 or 2) "))
        if pileChoice != 1 and pileChoice != 2:
            print(pileChoice, "is not a valid number")
    
        if pileChoice == 1:
            chipChoice = int(input("How many chips would you like to take from pile 1? "))
            if chipChoice > p1chips:  
                print ("\nPile 1 does not have that many chips. Try again.\n")
            elif chipChoice <= 0:
                print ("\nYou must take at least one chip\n")
                    
        elif pileChoice == 2:
            chipChoice = int(input("How many chips would you like to take from pile 2? "))
            if chipChoice > p2chips:  
                print ("\nPile 2 does not have that many chips. Try again.\n")
            elif chipChoice <= 0:
                print ("\nYou must take at least one chip\n")
                    
    print("That was a legal move. Thank you.\n")
    return pileChoice, chipChoice

# This is another function where it doesn't make sense to use doctest to figure out if it works properly;
# even though it has variable passed in and returned out, it relies on user input within the function
# to determine what values get passed out. This one was a bit harder to troubleshoot because it's more
# complicated than the functions that I'm used to writing. Still it is pretty easy to test by commenting
# out a large part of the main program. And leaving and printing the return values to isolate them. If they
# gave unexpected values that were incorrect I would go back inside the function and modify it. Also when I
# was running tests on the whole program and typing in the same input as the example givin in the pdf, I was
# able to double check that it was functioning properly, testing again with incorrect values such as 0 for
# how many chips to take from a pile, or trying to choose pile 3 for instance (a pile that does not exist).
#
# end of getHumanMove  
##########

##################
# 
def updatePiles(pileChosen, chipsChosen, p1chips, p2chips):
    """
    int, int, int, int -> int, int
    PRE:  Four parameters are passed to this function. (1) the pile chosen from, (2) the
          number of chips chosen from that pile, (3) the current count of chips in pile 1, (4) the
          current count of chips in pile 2
    POST: Two values are returned, namely, the count of chips in each pile after the move
    >>> updatePiles(1,3,5,6)
    (2, 6)
    >>> updatePiles(2,3,5,6)
    (5, 3)
    >>> updatePiles(1,5,7,6)
    (2, 6)
    >>> updatePiles(2,1,5,5)
    (5, 4)
    """
    if pileChosen == 1:
        p1chips = p1chips - chipsChosen
    else:
        p2chips = p2chips - chipsChosen
    
    return p1chips, p2chips
#
#end of updatePiles #########

##################
# 
def computerMove(localHumanPile, localHumanChips):
    """
    int, int -> int, int
    PRE:  Two parameters are passed to this function: (1) the pile the human chose from on her
          last turn, (2) the number of chips the human took on her last turn
    POST: The pile chosen by the computer, and the number of chips chosen by the computer are returned
    >>> computerMove(1,3)
    (2, 3)
    >>> computerMove(2,4)
    (1, 4)
    >>> computerMove(1,6)
    (2, 6)
    >>> computerMove(2,1)
    (1, 1)
    """
    if localHumanPile == 1:
        compPile = 2
    else:
        compPile = 1
    
    return compPile, localHumanChips
#
#end of computerMove  ###########

#MAIN PROGRAM
#

# if __name__ == "__main__": 
#     doctest.testmod()

print ("Welcome to the game of chips.  I know you know the rules so let's go.\n")

numChips = initializeGame()

pile1chips = numChips
pile2chips = numChips
gameOver = False

while not gameOver:
    print("Here are the piles ")
    displayPiles(pile1chips, pile2chips)
    print ("It is your turn.")
    
    humanPile, humanChips = getHumanMove(pile1chips, pile2chips)
    pile1chips, pile2chips = updatePiles(humanPile, humanChips, pile1chips, pile2chips)
    print("Here are the piles ")
    displayPiles(pile1chips, pile2chips)
    
    computerPile, computerChips = computerMove(humanPile, humanChips)
    pile1chips, pile2chips = updatePiles(computerPile, computerChips, pile1chips, pile2chips)
    print ("Now it is my turn. I'm thinking ...")
     
    time.sleep(3)    #This is just to slow things down a little.
    
    print ("I, the champion chips computer, will take", computerChips, "chips from pile", computerPile)
    if pile1chips == 0 and pile2chips == 0:
        gameOver = True

print ("The game is over and I won because I took the last chip.")
print ("Thanks for playing.  You wanna wager next time?")
