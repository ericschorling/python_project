# Level Dictionary:
# Here are the questions for Python Project - Level Dictonaries.

# Switched over to sub-class question:
class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        return self.question

# Question: 1

dict_question_1 = Question("computer_1 = {\n 'user': 'Sean',\n 'folder': 9,\n 'oh no': 'Enemy Found'\n}\nprint(computer_1.pop('oh no'))", "Enemy Found")


def play_question_1():
    print(dict_question_1.ask_question())
    answer = input("What will be printed? ")
    if answer == dict_question_1.answer:
        print("You remembered how to use .pop, to bad it didn't defeat the evil AI.")
    else:
        if answer is not dict_question_1.answer:
            print("You aren't even close, try again!")

play_question_1()
print()

# Question: 2

dict_question_2 = Question("player_skills = {\n   'DigitalCrafts':{\n      'programmer':{\n         'name': 'Sean',\n         'skills':{\n            'python': 70,\n            'git and github': -1,\n            'team work': 'Expert'\n         }\n       }\n     }\n   }\n print(player_skills['DigitalCrafts']['programmer']['name'])", "Sean")


def play_question_2():
    print(dict_question_2.ask_question())
    answer = input("What will be printed? ")
    if answer == dict_question_2.answer:
        print("Yep, you are right!")
    else:
        if answer is not dict_question_2.answer:
            print("No one by that name here, try again.")

play_question_2()
print()