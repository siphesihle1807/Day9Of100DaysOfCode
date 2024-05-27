import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
bid_completed = False

def highest_bidder(biddings):
    high_bid = 0 
    # initiates the bid
    winner = ""
    
    for bidder in biddings:
        bid_amount = biddings[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of R{high_bid}")

def bidding_process():
    global bid_completed
    while not bid_completed:
        bidder_name = input("Enter bidder's name: ")
        bidding_amount = int(input("How much would you like to bid: R"))
        bids[bidder_name] = bidding_amount
      # asks if there are any more bidders
      # ends the bid if there are none, returning the highest bidder and tge bidding amount
        bid_on = input("Are there any other bidders? y / n ? ")
        if bid_on == "n":
            bid_completed = True
            highest_bidder(bids)
        elif bid_on == "y":
          # clears the console for the next bidder.
            os.system('cls' if os.name == 'nt' else 'clear')

def play():
    bidding_process()

# Function is being called.
play()
