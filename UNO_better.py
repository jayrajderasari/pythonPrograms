# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 00:47:34 2022

@author: Jayraj Derasari
"""

import random
import os

"""Add Comments and Rules!"""

colours = ['b','y','r','g']         #defining possible colors
numbers = ['1','2','3','4','5','6','7','8','9','0','+4','s','w','r','+2']       #defining possible numbers for cards

deckOfCards = []

def creatingDeck():         #create a list as deck of cards to play with 
    for c in colours:
        for n in numbers:
            if n == '+4' or n == 'w':
                card = 'b' + n
                deckOfCards.append(card)
            elif n == '0':
                card = c + n
                deckOfCards.append(card)
            else:
                card = c + n
                for i in range(0,2):
                    deckOfCards.append(card)
    return deckOfCards


def distributeCards(noPlayers, noCards):        #to distribute cards among the players as list
    global playerCards
    global players
    n = 1
    while n <= noPlayers:
        cards = [0]*noCards
        for i in range(0,noCards): 
            cards[i] = pickACard()
        playerCards[n] = cards
        players.append(n)
        n = n + 1
    return playerCards

def pickACard():        #to randomly pick a card and remove that card from deck of cards
    card = random.choice(deckOfCards)
    deckOfCards.remove(card)
    return card
        
def checkColour():  #to check if the colour of card thrown is same as of uppercard
    global upperCard 
    if upperCard[0] == throw[0]:
        upperCard = throw
        return True        
    else:
        return False

def checkNumber():      #to check if the number of card thrown is same as uppercard or is +4 or wild
    global upperCard 
    if upperCard[1] == throw[1] or throw == 'b+4' or throw == 'bw':
        upperCard = throw
        return True        
    else:
        return False
    
def declareResult():        #to print results
    global noPlayers
    i = 0
    for i in range(0,noPlayers):
        if playerCards[players[i]]:    
            print (f"Player {players[i]} lose")
        else:
            print(f"Player {players[i]} wins")
 
creatingDeck()          #Creating a deck of UNO cards
upperCard= pickACard()  #assigning value to uppermost card
noCards = 7             # number of cards for each player in a match (7)
noPlayers = int(input("Enter number of Players:"))  #taking input of number of players
playerCards = {}    #dictionary to assign list of cards to each player as {playerNumber: [cards of player]}
                    
players = []        #list of names or player number of players
unoPlayers = []     # list of player declared UNO and have 1 card

while noPlayers>12:     #checking if the number of players are less than 12 as maximum 11 player can play at a time from one deck of cards
    print("Maximum 12 players can play at a time!")
    noPlayers = int(input("Enter number of Players:"))

playerCards = distributeCards(noPlayers, noCards)


def noCardsEach():          #to print number of cards each player have
    global noPlayers
    for showCards in range(0,noPlayers):
        show = players[showCards] 
        l = len(playerCards[show])
        print(f"Player {players[showCards]} has {l} cards")
    
def winCheck():     #to check if any player have 0 cards or not
    for i in range(0,noPlayers):
        if playerCards[players[i]]:
            winStatus = False
        else:
            winStatus = True
            break
    return winStatus

def colourChange():     #to change colour of upper card
    global upperCard
    colourChangeStatus = False
    while colourChangeStatus == False:
        newColour = str(input("Enter new colour:(blue / red / yellow / green)"))
        if newColour in colours:
            upperCard = upperCard + '-' + newColour[0]
            colourChangeStatus = True
        else:
            print("Enter appropriate colour")
    return upperCard

def caught():       # to catch a player if he have 1 card and has not declared UNO
    for i in range(0,noPlayers):
        i = players[i]
        if len(playerCards[i]) == 1 or unoPlayers:
            caught = str(input("Do you want to catch anyone?Y/N"))
            if caught == 'Y':
                playerCaught = int(input("Enter player number to be caught:"))
                if len(playerCards[playerCaught]) == 1 and playerCaught not in unoPlayers:
                    print("Caught")
                    for i in range(0,5): 
                        playerCards[playerCaught].append(pickACard())
                else:
                    print("Caught not valid")
                    break
            elif caught=='N':
                break
            
def unoCheck():     #to check if player is eligible to declare UNO and declare UNO
    if len(playerCards[players[currentPlayer]]) == 1:
        uno = str(input("Declare Uno?Y/N:"))
        if uno == 'Y':          
            print("UNO successful")
            unoPlayers.append(players[currentPlayer])
    
def currentUnoPlayers():        #to print players who have declared UNO
    global unoPlayers
    if unoPlayers:
        l = len(unoPlayers)
        for i in range(0,l):
            print("Player", unoPlayers[i], "has declared UNO!")

def changePlayer(no):       #to change the turn of player and clear screen
    global currentPlayer
    global noPlayer
    if currentPlayer+no<noPlayers:
        currentPlayer = currentPlayer + no
    else:
        currentPlayer = -1
        currentPlayer = currentPlayer + no
    os.system('cls')
    
    
currentPlayer = 0       #number of player whose turn it is
while currentPlayer != 'win':
    while currentPlayer in range(noPlayers) and winCheck() == False:
        player = str(input(f"Turn of Player {players[currentPlayer]}. Player {players[currentPlayer]} is there?Y/N:"))  
        #have confirmation that the player is such that his cards are not seen by anyone else
        
        noCardsEach()   #to display cards of each player
        
        currentUnoPlayers()     #to display number of UNO players
        
        print("Upper Card:", upperCard)  # print uppercard
        caught()        # catch players who didnt declare UNO and have 1 card
        if player == "Y":   #if player is present then continue his turn
        
            print("Your Cards:", playerCards[players[currentPlayer]]) #show cards of player
            throw = str(input("Enter card to throw or 'p' to pick a card:"))    #input of card to be thrown
            if throw in playerCards[players[currentPlayer]]:    #check if player have card he is trying to throw
                if checkColour() or checkNumber():  #check if card is relevent to upper card
                    playerCards[players[currentPlayer]].remove(throw)   #to remove card from list of card of players
                    deckOfCards.append(upperCard)       #add the card to the deck of remaining cards
                    upperCard = throw       #change the value of upper card
                    unoCheck()      #check if player is eligible for decalring UNO
                    if throw[1] == 's':     #to check if player has thrown skip card and change players accordingly
                        changePlayer(1)
                    elif throw[1] == '+' and throw[2] == '2':   #to check if player has thrown +2 card and change players accordingly
                        changePlayer(1) #to change turn of player
                        for n in range(0,2):    
                            playerCards[players[currentPlayer]].append(pickACard()) #penalise 2 cards to the next player
                    elif throw[1] == 'r':   #to check if player has thrown reverse card
                      changePlayer(1)   #change turn of player
                      players.reverse() #to reverse the list of players
                      currentPlayer = noPlayers - currentPlayer #to reverse loop appropriately
                    elif throw[1]=='+' and throw[2]=='4':   #to check if player has thrown +4
                        changePlayer(1)     #change turn of player
                        for n in range(0,4):    #penalise 4 cards to next player
                            playerCards[players[currentPlayer]].append(pickACard())     
                        colourChange()      #change colour of upper card
                    elif throw[1]=='w':     #to check if player has thrown wild card
                        colourChange()      #change colour of upper card
                    changePlayer(1)         #change turn of player
                else:       #if player has thrown inappropriate card
                    print("Enter proper card")
            elif throw == 'p':      #if player has chosen to pick a card
                playerCards[players[currentPlayer]].append(pickACard())     #add a card to cards of the player
                changePlayer(1) #change turn of player
            else:   #if player is trying to throw a card which he dont have
                print("Enter a card from your cards")  
        else:   #if player is not available
            print("Send Player", players[currentPlayer])   
    if winCheck() == True:     #to check If any one player have 0 cards
        print("Results:")
        declareResult()     #to declare winner and losers 
        currentPlayer = 'win'   #giving condition to end the while loop

