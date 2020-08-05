# Level class defines the behavior of each level and how it will be displayed during game play.

# class Level():
#     def __init__(self, question, answer, secret_code):
#         self.question = question
#         self.answer = answer
#         self.secret_code = secret_code

#     def ask_question(self):
#         return self.question

#     def prompt_for_answer(self):

# class LevelDict(Level):
#     def __init__(self, question, answer_prompt, answer, secret_code):
#         super().__init__(question, answer_prompt, answer, secret_code)

#     def ask_question(self):
#         super().ask_question()
#         self.question = "This is the output for the first question."

# list_question_1 = Level("for i in range (o, len(arr1))___",":", 1)


# print(list_question_1.ask_question())
# answer = input("What is the answer? ")
# if answer == list_question_1.answer:
#     print("You got it! \nThe secret code is %s" % (list_question_1.secret_code))