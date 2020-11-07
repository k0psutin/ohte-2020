class Player():
    def __init__(self, new_game=True):
        if new_game:
            self.player_credits = 10
            self.best_double_streak = 0
            self.current_streak = 0
            self.highscore = 0

        else:
            # TODO Load save
            pass

    def add_credits(self, amount):
        self.player_credits += amount

    def remove_credits(self, amount):
        self.player_credits -= amount

    def add_to_highscore(self, amount):
        self.player_credits += amount

    def succesful_double(self, succesful):
        if succesful:
            self.current_streak += 1
        else:
            self.best_double_streak = max(
                self.current_streak,
                self.best_double_streak)
            self.current_streak = 0
