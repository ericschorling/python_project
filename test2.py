class Question ():
    def __init__(self,question,answer, prompt):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.prompt = prompt
        #self.secret_code = secret_code
    def ask_question(self):           
            user_answer = "none"
            while user_answer != self.answer:
                print(self.question)
                user_answer = input(self.prompt)
                if user_answer == self.answer:
                    print("\nYou got it!" )
                elif user_answer != self.answer:
                    print("\nTry again")

