class Question ():
    def __init__(self,question,answer, prompt):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.prompt = prompt
        #self.secret_code = secret_code
    def ask_question(self, level):           
            user_answer = "none"
            while user_answer != self.answer:
                for line in self.question:
                    print(line)
                user_answer = input(self.prompt)
                if user_answer == self.answer:
                    print(level.get_correct() )
                elif user_answer != self.answer:
                    print("\nzzzt.. Incorrect, Ha. Ha. Ha.")

