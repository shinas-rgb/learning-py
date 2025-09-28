from data import question_data
from question_model import Question
from quiz_brain import Brain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))

question = Brain(question_bank)
for i in question_bank:
    question.next_question()


