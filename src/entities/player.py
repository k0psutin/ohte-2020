from repositories.player_repository import PlayerRepository


class Player():
    def __init__(self):
        self.credits = 10
        self.best_double_streak = 0
        self.best_double_win = 0
        self.best_credits = 10
        self.current_double_streak = 0
        self.player_repository = PlayerRepository()

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

    def save_player(self):
        save_data = {'credits': self.credits,
                     'best_double_streak': self.best_double_streak,
                     'best_double_win': self.best_double_win,
                     'best_credits': self.best_credits}

        if self.credits == 0:
            save_data = None

        self.player_repository.save(save_data)

    def load_player(self):
        save_data = self.player_repository.load()

        if save_data is None:
            return None

        self.credits = save_data['credits']
        self.best_double_streak = save_data['best_double_streak']
        self.best_double_win = save_data['best_double_win']
        self.best_credits = save_data['best_credits']

        return self
