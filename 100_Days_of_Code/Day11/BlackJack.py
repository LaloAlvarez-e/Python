import random
def BlackJackLogo():
    print('''
          .------..------..------..------..------..------..------..------..------.
          |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
          | :(): || :/\\: || (\\/) || :/\\: || :/\\: || :(): || (\\/) || :/\\: || :/\\: |
          | ()() || (__) || :\\/: || :\\/: || :\\/: || ()() || :\\/: || :\\/: || :\\/: |
          | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
          `------'`------'`------'`------'`------'`------'`------'`------'`------'
            ''')

backJackCards = {
    'A': {'value': 11, 'count': 4},
    '2': {'value': 2, 'count': 4},
    '3': {'value': 3, 'count': 4},
    '4': {'value': 4, 'count': 4},
    '5': {'value': 5, 'count': 4},
    '6': {'value': 6, 'count': 4},
    '7': {'value': 7, 'count': 4},
    '8': {'value': 8, 'count': 4},
    '9': {'value': 9, 'count': 4},
    '10': {'value': 10, 'count': 4},
    'J': {'value': 10, 'count': 4},
    'Q': {'value': 10, 'count': 4},
    'K': {'value': 10, 'count': 4},
    'Invalid': {'value': 0, 'count': 0}
}

def SearchCardToHand(hand):
    returnCode = 'Invalid'
    keyList = list(backJackCards.keys())
    cardFromDeck = random.choice(keyList)
    if(backJackCards[cardFromDeck]['count'] > 0):
        backJackCards[cardFromDeck]['count'] -= 1
        returnCode = cardFromDeck
    return returnCode

def SearchAndAppendCardToHand(hand):
    returnCode = False
    cardFromDeck = SearchCardToHand(hand)
    if('Invalid' != cardFromDeck):
        hand.append(cardFromDeck)
        returnCode = True
    return returnCode

def getCard(hand, cardCount):
    count = 0
    while count < cardCount:
        isAppended = SearchAndAppendCardToHand(hand)
        if(True == isAppended) :
            count += 1
    return hand

def getFirstHand(hand):
    hand = getCard(hand, 2)
    return hand

def calculateScore(hand):
    score = 0
    for card in hand:
        score += backJackCards[card]['value']
    return score

def main():
    BlackJackLogo()
    userHand = []
    computerHand = []
    getFirstHand(userHand)
    getFirstHand(computerHand)
    print(f"Your cards: {userHand}")
    print(f"Computer's first card: {computerHand[0]}")
    
    continuePlay = input("Do you want to draw another card? Type 'y' or 'n'\n")
    continuePlay = continuePlay.lower()
    userScore = calculateScore(userHand)
    computerScore = calculateScore(computerHand)
    while (continuePlay == "y"):
        getCard(userHand, 1)
        randomDesicion = random.choice(range(0,2))
        if((computerScore <= 11) or 
           ((randomDesicion == 1)) and (computerScore < 20)):
            print(f"Computer got a card")
            getCard(computerHand, 1)
        userScore = calculateScore(userHand)
        computerScore = calculateScore(computerHand)
        print(f"Your cards: {userHand} and score: {userScore}")
        if(userScore <= 21) :
            continuePlay = input("Do you want to draw another card? Type 'y' or 'n'\n")
            continuePlay = continuePlay.lower()
        else:
            continuePlay = "n"
    
    print(f"Your final hand: {userHand} and score: {userScore}")
    print(f"Computer's final hand: {computerHand} and score: {computerScore}")
    diffScore = userScore - computerScore
    if(userScore > 21):
        print("You went over. You lose")
    elif(computerScore > 21):
        print("Computer went over. You win")
    elif(diffScore > 0):
        print("You win")
    elif(diffScore == 0):
        print("It's a draw")
    else:
        print("You lose")
    
        
    
    
    
    # Your code here

if __name__ == "__main__":
    main()