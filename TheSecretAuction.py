print("Welcome to the secret auction! ")

#! We can include a feature in future which clears out the terminal each time a new user wants to place a bid
bids = {}

def auction(name, bid):
    bids[name] = bid    


bid = True

while bid:
    name = input("Enter Your Name: ")
    bid = int(input("Enter Your Bid: $"))

    auction(name, bid)


    user = input("Do you wanna place a bid?, Yes or No: \n")
    
    if user.lower() == 'no':
        bid = False
        
        highest_bid = 0
        highest_bidder = ""
        
        for bid in bids:
            if bids[bid] > highest_bid:
                highest_bid = bids[bid]
                highest_bidder = bid
        
        print(f"\n{highest_bidder} Wins the auction by bidding ${highest_bid}")
        break