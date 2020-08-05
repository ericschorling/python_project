# This will be the main game file. 
# Class level that will be the parent for all the levels. 

# Level class defines the behavior of each level and how it will be displayed during game play.

class Level():
    def __init__(self, question, answer, secret_code):
        self.question = question
        self.answer = answer
        self.secret_code = secret_code

    def ask_question(self):
        return self.question

    def prompt_for_answer(self):


# class Level1(Level):
#     def __init__(self, question, answer_prompt, answer, secret_code):
#         super().__init__(question, answer_prompt, answer, secret_code)

#     def ask_question(self):
#         super().ask_question()
#         self.question = "This is the output for the first question."