class GameStats():
    def __init__(self):  
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
        
    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.bonus = 0

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score