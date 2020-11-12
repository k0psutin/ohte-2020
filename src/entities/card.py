class Card:
    """Class that represent a single card.

    Attributes:

       value: An Integer, rank of the card. Min 2, max 14.

       suit: An Integer, value of the suit of the card. Min 1, max 4.

             1 = Hearts
             2 = Diamonds
             3 = Clubs
             4 = Spades

        color: A char, 'r' for red and 'b' for black.

        Typical usage example:

        Creates a playing card with value of 1 and suite of Hearts.
        card = Card(1, 1)
    """

    def __init__(self, rank, suit):
        """Constructor of the class. Creates a new playing card.

        Args:

            rank: An Integer, rank of the card. Min 1, max 13.

            suit: An Integer, value of the suit of the card. Min 1, max 4.

                1 = Hearts
                2 = Diamonds
                3 = Clubs
                4 = Spades

        Raises:

            Exception: If Card rank is not between (2,14).
            Exception: If Suit value is not between (1,4).
        """

        if rank < 2 or rank > 14:
            raise Exception(
                'The card rank should be between (2,14). The rank was %s'
                % (rank))

        if suit < 1 or suit > 4:
            raise Exception(
                'The card suit should be between (1,4). The suit was %s'
                % (rank))

        self.rank = rank
        self.suit = suit

        if suit in [1, 2]:
            self.color = 'r'

        else:
            self.color = 'b'

    def get_suit_type(self):
        """Returns the corresponding suit image filename

           Returns:

               Str: Image file name.
        """
        suit_type = {1: 'hearts.png',
                     2: 'diamonds.png',
                     3: 'clubs.png',
                     4: 'spades.png'}
        return suit_type[self.suit]

    def get_color_code(self):
        """Return the color code of the card. Used for card graphics.

           Returns:

               Color, suit color code

        """
        if self.color == 'r':
            return (254, 0, 0)
        else:
            return (0, 0, 0)

    def get_rank_type(self):
        """Return the suit type of the card. Used for card graphics.

           Returns:

               Str, string representation of the rank
        """
        rank_type = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

        if self.rank > 10:
            return rank_type[self.rank]
        else:
            return str(self.rank)

    def __str__(self):
        """String representation of the card object.

           Returns:

              String, Suite and the rank of the card.
        """

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
