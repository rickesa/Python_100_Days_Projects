auction_bids = {}
# debug strings below
# bidder = "name"
# amount = 12
# auction_bids[bidder] = amount
# bidder = "name2"
# amount = 14
# auction_bids[bidder] = amount
# bidder = "name3"
# amount = 11
# auction_bids[bidder] = amount
#
# print(auction_bids)

# def find_winner(auction_dictionary):  # simple method without ties
#     highest_bid = 0
#     for name in auction_bids:
#         if auction_bids[name] > highest_bid:
#             highest_bid = auction_bids[name]
#             bidder = name
#     print(f"the highest bid was ${highest_bid} made by {name}")


def find_winner(auction_dictionary):  # adding functionality to handle ties
    highest_bid = 0
    bidder = ""
    tied_bidders = []
    tie_bid = 0
    for name in auction_bids:
        if auction_bids[name] > highest_bid:
            highest_bid = auction_bids[name]
            bidder = name
        elif auction_bids[name] == highest_bid:
          tied_bidders.append(name)
          tie_bid = auction_bids[name]
    if len(tied_bidders) >= 1 and tie_bid == highest_bid:
        print(f"There were multiple bidders tied at ${tie_bid}")
    else:
        print(f"the highest bid was ${highest_bid} made by {bidder}")


def build_auction():
    bidding_finished = False
    while not bidding_finished:
        bidder = input("What is the bidder's name?\n")
        amount = int(input("What is the bid amount?\n"))
        auction_bids[bidder] = amount
        again = input("Is there another bidder? Type y or n\n").lower()
        if again == 'n':
            bidding_finished = True
    find_winner(auction_bids)


build_auction()
