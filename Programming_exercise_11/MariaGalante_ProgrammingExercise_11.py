import random



# Deck Class

class Deck:
    """
    Creates and manages a deck of playing cards.

    Variables:
        cards (list): stores all cards in the deck

    Logic:
        - Create 52-card deck using suits and ranks
        - Shuffle deck randomly

    Return:
        None
    """


    def __init__(self):
        # Create deck using unicode suits
        self.cards = [rank + suit
                      for suit in '\u2665\u2666\u2663\u2660'
                      for rank in 'A23456789TJQK']


        # Shuffle the deck to randomize order
        random.shuffle(self.cards)

    def deal_card(self):
        """
        Removes and returns the top card from the deck.

        Return:
            str: a single card
        """
        return self.cards.pop()




# Deal Hand Function

def deal_hand(deck):
    """
    Deals 5 cards from the deck.

    Parameters:
        deck (Deck): the deck object

    Variables:
        hand (list): stores the dealt cards

    Logic:
        - Loop 5 times
        - Add one card each time

    Return:
        list: list of 5 cards
    """

    hand = []

    # Loop to deal 5 cards
    for _ in range(5):
        hand.append(deck.deal_card())

    return hand



# Show Hand Function

def show_hand(hand):
    """
    Displays the player's hand.

    Parameters:
        hand (list): list of cards

    Return:
        None
    """

    print("\nYour hand:")

    # Display each card with position number
    for index, card in enumerate(hand, start=1):
        print(f"{index}: {card}")



# Replace Cards Function

def replace_cards(deck, hand):
    """
    Replaces selected cards in the hand.

    Parameters:
        deck (Deck): the deck object
        hand (list): player's current hand

    Variables:
        choices (str): user input
        indexes (list): parsed positions

    Logic:
        - Ask user which cards to replace
        - Convert input into positions
        - Replace selected cards

    Return:
        list: updated hand
    """

    # Prompt user for input
    choices = input(
        "\nEnter card positions to replace "
        "(example: 1 3 5), or press Enter to keep all: "
    )

    # If user presses Enter, keep same hand
    if choices.strip() == "":
        return hand

    indexes = choices.split()

    # Replace selected cards
    for index in indexes:
        i = int(index) - 1

        if 0 <= i < len(hand):
            hand[i] = deck.deal_card()

    return hand



# Main Game Function

def play_poker():
    """
    Runs the poker game.

    Logic:
        - Create deck
        - Deal initial hand
        - Show hand
        - Replace cards
        - Show final hand

    Return:
        None
    """

    # Create a new deck
    deck = Deck()

    # Deal initial hand
    hand = deal_hand(deck)

    # Display initial hand
    show_hand(hand)

    # Replace selected cards
    hand = replace_cards(deck, hand)

    # Display final hand
    print("\nFinal hand:")
    show_hand(hand)



# Program Entry Point
if __name__ == "__main__":
    # Run the poker game
    play_poker()