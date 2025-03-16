# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)



def find_highest_bidder(bidding_dictionary):
    winner = " "
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount >= highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the bid of ${highest_bidder}")

bids = {}
continue_bidding = True
while continue_bidding == True:
    print("welcome to secret auction")
    name = input("What is your name?\n")
    price = int(input("What is your bid: $\n"))
    bids[name]= price
    should_continue = input("Are there more bidders? Type yes or no\n")
    print("\n" * 10000)
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
