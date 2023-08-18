class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.read_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        with open('save.txt') as file_object:
            contents = file_object.read()
            return(int(contents[11:]))

    def write_high_score(self):
        self.filename = 'save.txt'
        with open(self.filename, 'w') as file_object:
            file_object.write(f"high_score={self.high_score}")