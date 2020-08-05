# Level lists:
# Here are the questions for Python Project - Level Lists.

# Parent class.
class Level():
    def __init__(self, question, answer, secret_code):
        self.question = question
        self.answer = answer
        self.secret_code = secret_code

    def ask_question(self):
        return self.question

list_question_1 = Level("list = ['The cat knows code', 'She worked as a Project Manager before attending DigitalCrafts', 'Today is not yesterday!']\n clue1 = (list[0])\n clue2 = (list[0])\n clue3 = (list[1])\n clue4 = (list[2])\n print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[13:24])", "The code worked yesterday!", "tbd")

# Add secret answer above ^

def play_question_1():
    print(list_question_1.ask_question())
    answer = input("What is the output? ")
    if answer == list_question_1.answer:
        print("You got it! \nThe secret code is %s" % (list_question_1.secret_code))
    else:
        if answer is not list_question_1.answer:
            print("You aren't even close, try again!")

play_question_1()

# Question 2:

# list_question_2 = Level("Question", "Answer", "tbd")

# # Add secret answer above ^

# def play_question_2():
#     print(list_question_1.ask_question())
#     answer = input("What is the output? ")
#     if answer == list_question_1.answer:
#         print("Wow you are on a roll! \nThe secret code is %s" % (list_question_2.secret_code))
#     else:
#         if answer is not list_question_2.answer:
#             print("That's not right, try again!")

# play_question_2()