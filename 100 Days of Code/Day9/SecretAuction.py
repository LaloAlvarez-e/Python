from replit import clear

def BidLogo():
    print('''
           ___________
                    /
            )_______(
            |"""""""|_.-._,.---------.,_.-._
            |       | | |               | | ''-.
            |       |_| |_             _| |_..-'
            |_______| '-\'''---------'' '-'
            )"""""""(
            /_________\\
         .-------------.
        /_______________\\
          ''')
    print("Welcome to the secret auction program.")

bidders = {}

def GetMaxBidder(bidders):
    higherBid = 0.0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > higherBid:
            higherBid = bidders[bidder]
            winner = bidder
    return (winner, higherBid)

def main():
    # Your code here
    BidLogo()
    running = True
    while running:
        name = input("What is your name?: ")
        bid = input("What's your bid?: $")
        
        try:
            bid = float(bid)
            if  name in bidders:
                oldBid = bidders[name]
                if(bid > oldBid):
                    print(f"Name already exists, overwriting the bid... from ${oldBid} to ${bid}")
                else:
                    bid = oldBid
                    print(f"Name already exists, keeping the old bid of ${oldBid}")
            
            bidders[name] = bid
        except:
            print(f"Invalid bid for {name}, please enter a valid bid number")
        
        
        isNewBidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        isNewBidder = isNewBidder.lower()
        if(isNewBidder != 'yes'):
            running = False
        else:
            clear()
    
    
    winner, higherBid = GetMaxBidder(bidders)
    print(f"The winner is {winner} with a bid of ${higherBid}")
    
    

if __name__ == "__main__":
    main()    # Your code here