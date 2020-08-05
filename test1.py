#Classes for python project
class Level():
    def __init__(self,question,answer,secret_code):
        self.question = question 
        # self.answer_prompt = answer_prompt
        self.answer = answer
        self.secret_code = secret_code
    
    def ask_question(self):
        return self.question 


#question1 = Level("\n___ add(num1, num2):\n   return num1 + num2\n","def",1)
#question1 = Level("\ndef add(num1_ num2):\n   return num1 + num2\n",",",2)
#question1 = Level("\ndef add_num1, num2):\n   return num1 + num2\n","(",3)
#question1 = Level("\ndef add(num1, num2_:\n   return num1 + num2\n",")",4)
#question1 = Level("\ndef add(num1, num2)_\n  return num1 + num2\n",":",5)
#question1 = Level("\ndef add(num1, num2):\n ____return num1 + num2\n","    ",6)
#question1 = Level("\ndef add(num1, num2)_\n  ______ num1 + num2\n","return",7)
#question1 = Level("\ndef add(__________):\n    return num1 + num2\n","num1, num2",8)
question1 = Level("\ndef add(num1, num2):\n    return num1 + num2\n\nsum = ___(1,1)\nprint(sum)\n","add",9)

answer = "none"
while answer != question1.answer:
    secret_code = True
    if secret_code is True:
        print(question1.ask_question())
        answer = input("Fill in the blank?\n")
    if answer == question1.answer:
        print("\nYou got it! \nThe secret code is %s" % (question1.secret_code) )
    elif answer != question1.answer:
        print("\nTry again")

