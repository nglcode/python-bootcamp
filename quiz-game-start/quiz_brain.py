class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        question = self.questions_list[self.question_number]
        input(f"Q.{self.question_number+1}: {question.text} (True/False): ")
        self.question_number += 1

    def still_has_questions(self):
        return len(self.questions_list) > self.question_number