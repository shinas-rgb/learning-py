class Score:
    def __init__(self):
        self.score = 0
        try:
            with open("high_score.txt", "r") as file:
                content = file.read().strip()
                self.highScore = int(content) if content else 0
        except (ValueError, FileNotFoundError):
            self.highScore = 0
            with open("high_score.txt", "w") as file:
                file.write("0")

    def high_score(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))


    def new_score(self):
        self.score += 1
