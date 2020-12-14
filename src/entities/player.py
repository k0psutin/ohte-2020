"""Module player.py

    This module is used to create an instance of a Player-class.
    """


class Player():
    """Class that represents the player.

    This class is responsible for maintaining player related variables,
    such as credits and highscores.

    Calling the constructor, it sets the default variables for a new player,
    and creates an instance of Player Repository, for handling savegames.

    Typical usage example:
        player = Player()
    """

    def __init__(self):
        """Constructor of the class. Sets values for new player.
        """
        self.credits = 10
        self.best_double_streak = 0
        self.best_double_win = 0
        self.best_credits = 10
        self.current_double_streak = 0

    def double_win(self, amount):
        """Update player stats upon claiming wins from doubling

        Args:

            amount (int): Credit amount.
        """
        self.best_double_streak = max(
            self.current_double_streak,
            self.best_double_streak)
        self.best_double_win = max(amount, self.best_double_win)
        self.current_double_streak = 0

    def add_credits(self, amount):
        """Adds credits to player and keeps track of the current best credit.

        Args:

            amount (int): The amount that will be
                    added to current credits.

        Typical usage example:

            Add 10 credits to player.
            add_credits(10)
        """
        self.credits += amount
        self.best_credits = max(
            self.credits,
            self.best_credits)

    def remove_credits(self, amount):
        """Removes credits from player. If amount is more than
           players current credits, remove remaining credits from player.

        Args:

            amount (int): The amount that will be subtracted from player.

        Typical usage example:

            Remove 5 credits from player.
            remove_credits(5)
        """
        if self.credits < amount:
            amount = self.credits
        self.credits -= amount

    def successful_double(self, successful):
        """Manages current double streak and checks if it is a new best streak.

        Args:

            successful (bool): If True, add one more to streak.
            Otherwise checks if current streak is the best
            and resets the counter.

        Typical usage example:

            Player succesfully guesses the card.
            successful_double(True)
        """
        if successful:
            self.current_double_streak += 1
        else:
            self.current_double_streak = 0
