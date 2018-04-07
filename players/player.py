class Player:

    def __init__(self):
        self.wins = 0

    def add_a_win(self):
        self.wins += 1

    def get_wins(self):
        return self.wins