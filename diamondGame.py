import random

# Define card values
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Define suits
SUITS = ['Hearts', 'Clubs', 'Spades']

# Define number of diamond cards
DIAMOND_CARDS_COUNT = 13

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.points = 0

    def assign_cards(self, cards):
        self.hand = cards

    def bid(self):
        print(f"\n{self.name}'s Hand:")
        for index, card in enumerate(self.hand, start=1):
            print(f"{index}. {card}")
        while True:
            bid_card_index = int(input(f"{self.name}, select the index of the card to bid (e.g., 1, 2, 3...): ")) - 1
            if 0 <= bid_card_index < len(self.hand):
                bid_card = self.hand.pop(bid_card_index)
                return bid_card
            else:
                print("Invalid index. Please choose a valid index.")

def initialize_deck():
    deck = []
    for suit in SUITS:
        for value in CARD_VALUES:
            card = f"{value} {suit}"
            deck.append(card)
    random.shuffle(deck)
    return deck

def divide_cards(players, deck):
    cards_per_player = len(deck) // len(players)
    for player in players:
        player.assign_cards(deck[:cards_per_player])
        deck = deck[cards_per_player:]
    return players

def show_scorecard(players):
    print("\nScorecard:")
    for player in players:
        print(f"{player.name}: {player.points} points")

def play_game(players):
    deck = initialize_deck()
    players = divide_cards(players, deck)

    diamond_cards = random.sample([f"{value} Diamonds" for value in CARD_VALUES.keys()], DIAMOND_CARDS_COUNT)

    for diamond_card in diamond_cards:
        print("\nAuctioning diamond card:", diamond_card)
        bids = {player.name: player.bid() for player in players}

        max_bid_value = max([CARD_VALUES[bid.split()[0]] for bid in bids.values()])
        winners = [player for player, bid_card in bids.items() if CARD_VALUES[bid_card.split()[0]] == max_bid_value]

        if len(winners) == 1:
            winning_player = [player for player in players if player.name == winners[0]][0]
            winning_player.points += CARD_VALUES[diamond_card.split()[0]]
            print(f"{winning_player.name} wins the bid and gets {CARD_VALUES[diamond_card.split()[0]]} points!")
        else:
            points_per_winner = CARD_VALUES[diamond_card.split()[0]] / len(winners)
            for winner in winners:
                winning_player = [player for player in players if player.name == winner][0]
                winning_player.points += points_per_winner
                print(f"{winning_player.name} ties for the bid and gets {points_per_winner:.2f} points!")

        show_scorecard(players)

    print("\nGame Over!")
    print("Final Scores:")
    show_scorecard(players)

def main():
    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter player {i+1}'s name: ")) for i in range(num_players)]
    play_game(players)

if __name__ == "__main__":
    main()
