#Classes for python project
#Level class defines the behavior of each level and how it will be displayed during game play
class Level():
    def __init__(self, question, answer, secret_code):
        self.question = question
        
        #self.answer_prompt = answer_prompt
        self.answer = answer
        self.secret_code = secret_code
        #levels could each have reponses from the enemy AI as part of the code. 
        #levels need to have a snippet of code that takes an answer and runs it against previous code, this could be in a function.
    #def set_question(self):
    #    self.question = "This is where the question goes"

    def get_question(self):
        return self.question


class Level2(Level):
    def __init__(self,question,answer,secret_code, AI_catchphrase):
        super().__init__(question, answer,secret_code)
        self.AI_catchphrase = AI_catchphrase
        self.answer = "elif x == 11:"
        self.secret_code = "d1r0w 0113h"
        self.question = "if x > 10:\n    print(\"Q_3 code\")\nelse x = 11:\n   print(\"correct code\")\n else:\n    print(\"destroy building\")"

    def solve_question(self):
        n = 10
        x = 2 + n + 4 - 5
        if x > 10:
            return "wrong code"
        elif x == 11:
            return "correct code"
        else: 
            return "destory building"

    def check_solution(self, player_ans):
        player_ans == self.answer


#character Class
class Player():
    def __init__(self, name, shirt_color, catch_phrase):
        self.name = name
        self.shirt_color = shirt_color
        self.catch_phrase = catch_phrase
#add notebook class to take all the codes and store them
#create menu class?
#does it have any attributes? 
#Will it need to battle the AI somehow?

#question_array=[question_1, question_2]
    
#class Level1(Level):
#    def __init__(self, question, answer_prompt, answer, secret_code):
#        super().__init__(question, answer_prompt,answer,secret_code)#

#    def ask_question(self):
#        super().ask_question()
#        self.question = "This is the output for the first question"


#        """for x in arr:
#        new_arr = arr[-x]"""
#dlrow olloh 
#question ="For i in array:
#            arr_2[i] = array[i]"

#            what's wrong with the code
#            -i  =answer
#            output hello world 
#            your secret code is asdfadsfa

