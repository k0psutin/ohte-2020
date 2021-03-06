"""Module card.py

    This module is used to create an instance of Card-class.
    """

from entities.suit import Suit


class Card:
    """Class that represent a single card.

    Attributes:

       value (int): An Integer, rank of the card. Min 2, max 14.

       suit (enum): An enum, representing the suite of the card.

        color: A char, 'r' for red and 'b' for black.

        Typical usage example:

        Creates a playing card with value of 1 and suite of Hearts.
        card = Card(1, Suite.hearts)
    """

    def __init__(self, rank, suit):
        """Constructor of the class. Creates a new playing card.

        Args:

            rank (int): The rank of the card. Min 1, max 13.
            suit (enum): An enum, representing the suit of the card.

        Raises:

            Exception: If Card rank is not between (2,14).
            Exception: If Suit is not in
        """

        if rank < 2 or rank > 14:
            raise Exception(
                'The card rank should be between (2,14). The rank was %s'
                % (rank))

        if suit not in Suit:
            raise Exception(
                'Invalid card suite. The suite was %s'
                % (suit))

        self.rank = rank
        self.suit = suit

        if suit in [Suit.hearts, Suit.diamonds]:
            self.color = 'r'

        else:
            self.color = 'b'

    def get_suit_type(self):
        """Returns the corresponding suit image filename

           Returns:

               str: Image file name.
        """
        suit_type = {Suit.hearts: 'hearts.png',
                     Suit.diamonds: 'diamonds.png',
                     Suit.clubs: 'clubs.png',
                     Suit.spades: 'spades.png'}
        return suit_type[self.suit]

    def get_color_code(self):
        """Return the color code of the card. Used for card graphics.

           Returns:

               color: suit color code

        """
        if self.color == 'r':
            return (254, 0, 0)
        else:
            return (0, 0, 0)

    def get_rank_type(self):
        """Return the suit type of the card. Used for card graphics.

           Returns:

               str: A string representation of the rank
        """
        rank_type = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

        if self.rank > 10:
            return rank_type[self.rank]
        else:
            return str(self.rank)

    def __str__(self):
        return f'Rank: {self.rank}, Suit: {self.suit}'

    def __eq__(self, other: 'Card'):
        if other is None:
            return False

        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: 'Card'):
        return self.rank < other.rank

    def __le__(self, other: 'Card'):
        return self.rank <= other.rank

    def __gt__(self, other: 'Card'):
        return self.rank > other.rank

    def __ge__(self, other: 'Card'):
        return self.rank >= other.rank
