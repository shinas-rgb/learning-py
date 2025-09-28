class Brain:
    def __init__(self, qlist):
        self.q_num = 0
        self.q_list = qlist
        self.score = 0

    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        ans = input(f"{self.q_num}: {current_q.text}\nA: ")
        if ans == current_q.answer:
            self.score += 1
            print(f"right! ({self.score}/{self.q_num})")
        else:
            print(f"wrong! ({self.score}/{self.q_num})")
