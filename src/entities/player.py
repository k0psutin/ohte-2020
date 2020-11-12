class Player():
    def __init__(self, new_game=True):

        if new_game:
            self.credits = 10
            self.best_double_streak = 0
            self.best_double_win = 0
            self.best_credits = 10

            self.current_double_streak = 0

        else:
            # TODO Load save
            raise Exception('Loading old save is not implemented yet.')

    def add_credits(self, amount):
        self.credits += amount
        self.best_credits = max(
            self.credits,
            self.best_credits)

    def remove_credits(self, amount):
        if self.credits < amount:
            amount = self.credits
        self.credits -= amount

    def successful_double(self, succesful):
        if succesful:
            self.current_double_streak += 1
        else:
            self.best_double_streak = max(
                self.current_double_streak,
                self.best_double_streak)
            self.current_double_streak = 0
