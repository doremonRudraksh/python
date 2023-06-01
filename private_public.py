class Score:
    def __init__(self):
        self.__score = 1

    def print_score(self):
        print(self.__score)

    def score_update(self):
        self.__score += 1
        print(self.__score)

player = Score()
player.score=100
player.score_update()
player.score_update()
