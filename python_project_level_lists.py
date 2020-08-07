# Level lists:
# Here are the questions for Python Project - Level Lists.

# Switched over to sub-class question:
class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        return self.question

# Question: 1

list_question_1 = Question("list = ['The cat knows code', 'She worked as a Project Manager before attending DigitalCrafts', 'Today is not yesterday!']\n clue1 = (list[0])\n clue2 = (list[0])\n clue3 = (list[1])\n clue4 = (list[2])\n print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[13:24])", "The code worked yesterday!")


def play_question_1():
    print(list_question_1.ask_question())
    answer = input("What is the output? ")
    if answer == list_question_1.answer:
        print("You got it!")
    else:
        if answer is not list_question_1.answer:
            print("You aren't even close, try again!")

play_question_1()

# Question: 2

list_question_2 = Question("list2 = ['The', 'REASON', 'your', 'CODE', 'IS', 'NOT', 'working today....']\n letter_1 = (list2[1]\n letter_2 = (list2[4])\n print('The ' + letter_1[2] + letter_2[0] + ' has leveled up and is now in contol of computer #.')", "AI")


def play_question_2():
    print(list_question_2.ask_question())
    answer = input("What is the output? ")
    if answer == list_question_2.answer:
        print("The output revealed: The AI has leveled up and is now in contol of computer #.")
        print("That's right! You're one step closer to defeating the AI.")
    else:
        if answer is not list_question_2.answer:
            print("Not quite, try again!")

play_question_2()

# Question: 3

list_question_3 = Question("list3 = ['d1r0w', '0113h']\n list3.reverse()\n print(list3)", "hello world")


def play_question_3():
    print(list_question_3.ask_question())
    answer = input("Reorder the output to convert this Leet Speak? ")
    if answer == list_question_3.answer:
        print("You are a natural, join Sean AI in the DC Hall of Fame!")
    else:
        if answer is not list_question_3.answer:
            print("Maybe you need a translator, try again!!")

play_question_3()