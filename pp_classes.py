#Classes for python project
#Level class defines the behavior of each level and how it will be displayed during game play
import random 

class Level():
    def __init__(self,secret_code):
        self.secret_code = secret_code

  
    def get_correct(self):
        correct_array = ["Awesome", 'You got it', 'way to go!!', 'we\'re getting there!', 'Let\'s crush that AI!']
        return correct_array[random.randint(0,len(correct_array)-1)]
