import random

# Function to roll the dice
def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

# Function to display dice
def display_dice(dice):
    print("Dice:", dice)

# Function to choose which dice to keep for reroll
def choose_dice(dice):
    choices = input("Enter dice values to keep (e.g., 1 3 4), or 'none' to reroll all: ").strip().split()
    if choices == ['none']:
        return roll_dice()
    else:
        choices = [int(choice) for choice in choices]
        return [die if index + 1 in choices else roll_dice()[index] for index, die in enumerate(dice)]

# Function to calculate score for a given category
def calculate_score(category, dice):
    if category in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]:
        return sum(die for die in dice if die == int(category))
    elif category == "Three of a Kind" or category == "Four of a Kind" or category == "Chance":
        return sum(dice)
    elif category == "Full House":
        return 25 if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3) else 0
    elif category == "Small Straight":
        return 30 if len(set(dice)) >= 4 and (1 in dice and 2 in dice and 3 in dice and 4 in dice) else 0
    elif category == "Large Straight":
        return 40 if len(set(dice)) == 5 and (1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice) else 0
    elif category == "Yahtzee":
        return 50 if len(set(dice)) == 1 else 0
    else:
        return 0

# Function to display scoring categories and their methods
def display_scoring_methods(categories):
    print("\nScoring methods:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}: {get_scoring_method(category)}")

# Function to get scoring method for a category
def get_scoring_method(category):
    if category in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]:
        return "Sum of dice with matching number"
    elif category in ["Three of a Kind", "Four of a Kind", "Chance"]:
        return "Sum of all dice"
    elif category == "Full House":
        return "25 points for a full house"
    elif category == "Small Straight":
        return "30 points for a small straight"
    elif category == "Large Straight":
        return "40 points for a large straight"
    elif category == "Yahtzee":
        return "50 points for a yahtzee"
    else:
        return "Custom scoring method"  # Add custom scoring methods if necessary

# Function to display scoring categories
def display_categories(categories):
    print("\nAvailable scoring categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

# Main function to play the game
def play_yahtzee():
    print("Welcome to Yahtzee!")

    # Initialize players and their scores
    num_players = int(input("Enter number of players: "))
    players = {input(f"Enter name for player {i+1}: "): {'total_score': 0} for i in range(num_players)}

    # Initialize game variables
    categories = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Three of a Kind", "Four of a Kind",
                  "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance"]
    rounds = 13

    # Display scoring methods
    display_scoring_methods(categories)

    # Main game loop
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}!\n")
        for player, scorecard in players.items():
            print(f"\n{player}'s turn:")
            dice = roll_dice()
            display_dice(dice)

            # Reroll up to three times
            for reroll in range(3):
                dice = choose_dice(dice)
                display_dice(dice)

                if reroll == 2:
                    break

                choice = input("Enter 'none' to keep these dice or any key to reroll: ").strip()
                if choice == 'none':
                    break

            # Prompt player to choose category
            display_categories(categories)
            category_choice = int(input("Choose a category number to score your roll: "))
            category = categories[category_choice - 1]

            # Score the roll
            score = calculate_score(category, dice)
            scorecard[category] = score
            total_score = sum(scorecard.values())
            scorecard['total_score'] = total_score
            print("Scorecard:", scorecard)

        # Display current total score of each player
        print("\nCurrent Total Scores:")
        for player, scorecard in players.items():
            print(f"{player}: {scorecard['total_score']}")

    # Display final scores
    print("\nFinal Scores:")
    for player, scorecard in players.items():
        print(f"{player}: {scorecard['total_score']}")

# Run the game
if __name__ == "__main__":
    play_yahtzee()
