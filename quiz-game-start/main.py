from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data_item in question_data:
    question_text = data_item["text"]
    question_answer = data_item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()
