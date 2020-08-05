class Question ():
    def __init__(self,question,answer,secret_code):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.secret_code = secret_code
    def ask_question(self):           
            user_answer = "none"
            while user_answer != self.answer:
                secret_code = True
                if secret_code is True:
                    print(self.question)
                    user_answer = input("Fill in the blank?\n")
                    if user_answer == self.answer:
                        print("\nYou got it! \nThe secret code is %s" % (self.secret_code) )
                    elif user_answer != self.answer:
                        print("\nTry again")

question1 = Question("\n___ add(num1, num2):\n   return num1 + num2\n","def",1)
question2 = Question("\ndef add(num1_ num2):\n   return num1 + num2\n",",",2)
question3 = Question("\ndef add_num1, num2):\n   return num1 + num2\n","(",3)
question4 = Question("\ndef add(num1, num2_:\n   return num1 + num2\n",")",4)
question5 = Question("\ndef add(num1, num2)_\n  return num1 + num2\n",":",5)
question6 = Question("\ndef add(num1, num2):\n ____return num1 + num2\n","    ",6)
question7 = Question("\ndef add(num1, num2)_\n  ______ num1 + num2\n","return",7)
question8 = Question("\ndef add(__________):\n    return num1 + num2\n","num1, num2",8)
question9 = Question("\ndef add(num1, num2):\n    return num1 + num2\n\nsum = ___(1,1)\nprint(sum)\n","add",9)




question1.ask_question()
question2.ask_question()
question3.ask_question()
question4.ask_question()
question5.ask_question()
question6.ask_question()
question7.ask_question()
question8.ask_question()
question9.ask_question()


