#Classes for python project
class Level():
    def __init__(self,question,answer,secret_code):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.secret_code = secret_code
    
    def ask_question(self):
        return self.question 



question1 = Level("\n___ add(num1, num2):\n   return num1 + num2","def",1)


print(question1.ask_question())


answer = input("what's the answer?")
if answer == question1.answer:
    print("You got it! \nThe secret code is %s" % (question1.secret_code) )
