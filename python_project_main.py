#This will be the main game file.
#class level that will be the parent for all the levels 
#import statements.
#Pulls in random for x
#pulls in classes defined in PP_Classes used for questions and levels
import random
from pp_classes import Level
#from pp_classes import Player
from test2 import Question
import pygame
import pygame.font
import pygame.event
import pygame.draw
import os
import sys
from pygame.locals import * 

#QUESTION_1= "SEAN_AI: Need to fix this print statement:\nprint('destroy all humans'"
#ANSWER_PROMPT = "Tell me your answer"
# questions initialized
TOTAL_LEVELS = 4
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# x = 0
# y = 0
# code_string = ""
# secret_ans_array = []

pygame.init()

# player Classe
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player(pygame.sprite.Sprite):
    def __init__(self,name, shirt_color, catch_phrase ):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75,25))
        #self.surf.fill((255,255,255))
        ##Adding a pic
        self.name = name
        self.shirt_color = shirt_color
        self.catch_phrase = catch_phrase
        self.surf = pygame.image.load("player_right.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect()
    #moving based on keystrokes
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.surf = pygame.image.load("player_up.png").convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.surf = pygame.image.load("player_down.png").convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.surf = pygame.image.load("player_left.png").convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.surf = pygame.image.load("player_right.png").convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
        #keep player on the board
        #left side can't be less than the left side 0 point
        if self.rect.left < 0:
            self.rect.left = 0
        #rightside can't be great than the width
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        #top can't be less than 0
        if self.rect.top <= 0:
            self.rect.top = 0
        #bottom can't go above the top
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#Creates randomized strings that are used as the secret codes, we wouldn't want to cheat...

def gen_codes(levels_in_game):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = 0
    y = 0
    code_string = ""
    secret_ans_array = []
    while x < levels_in_game:
        while y < random.randint(8,16):
            code_val = random.randint(0,62)
            if code_val < 26:
                code_string += alphabet[code_val]
            elif code_val >= 26 and code_val < 52:
                code_string += alphabet[code_val - 26].upper()
            else:
                code_string += str(random.randint(0,9))
            y += 1
        y = 0
        secret_ans_array.append(code_string)
        code_string = ""
        x += 1
    return secret_ans_array
ans_array = gen_codes(TOTAL_LEVELS)
def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass
#Takes 5 arguments Screen, a message to display, a screen size for the background, and a screen setup for the outline. Also takes an argument for font size.
def display_box_no_input(screen, message,fore_ground, outline_box):
    #"Print a message in a box in the middle of the screen"
    #This sets the background for the text input. 
    fontobject = pygame.font.Font(None, 30)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      screen.get_height() - 60,
                      400, 54), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                      ((screen.get_width() / 2) - 102,
                       screen.get_height() - 68,
                       404, 60), 1)
    #This displays the messages
    screen.blit(fontobject.render(message, 1, (255, 255, 255)),
        ((screen.get_width() / 2) - 100, screen.get_height() - 30))
            
    pygame.display.flip()
    while True:
        a_key = get_key()
        if a_key == K_RETURN:
            break
#THis is used to ask for input from the user and doesn't need a key press to close

def display_box(screen, message,screen1_info, screen2_info):
    #"Print a message in a box in the middle of the screen"
    #This sets the background for the text input. 
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      screen.get_height() - 60,
                      400, 54), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                      ((screen.get_width() / 2) - 102,
                       screen.get_height() - 68,
                       404, 60), 1)
    #This displays the messages
    screen.blit(fontobject.render(message, 1, (255, 255, 255)),
        ((screen.get_width() / 2) - 100, screen.get_height() - 30))
            
    pygame.display.flip()
    # while True:
    #     a_key = get_key()
    #     if a_key == K_RETURN:
    #         break
def ask(screen, question): 
    #"ask(screen, question) -> answer"
    pygame.font.init()        
    current_string = []
    display_box(screen, question + "".join(current_string),1,1)
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            # file = open(bad_words_file, 'r').readlines()
            # if "".join(current_string) in [thing[:-1] for thing in file]:
            #     current_string = []
            # else:
            break
        # elif inkey == K_MINUS:
        #     current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string),1,1)
    return "".join(current_string)
#def a message display function for placing text on the screen
#nput("Tell me something:")

#Create the level objects that carry the random encouragement and the secret answer
print(ans_array)
lvl1= Level(ans_array[0])
lvl2= Level(ans_array[1])
lvl3= Level(ans_array[2])
lvl4= Level(ans_array[3])
level_arr = [lvl1,lvl2,lvl3, lvl4]

#Prompts for the asnwers, different by question and level
LVL_2_PROMPT = "Fix the line of code.\n "
LVL_4_PROMPT = 'Enter missing code\n'
LVL_1_PROMPT = "Solve the riddle with code provided\n"

#Since each question is an object we have to initialize them all here.
#Level 1 question initialized
list_question_1 = Question(["list = ['The cat knows code', 'She worked as a Project Manager before attending DigitalCrafts', 'Today is not yesterday!']", "clue1 = (list[0])", "clue2 = (list[0])", "clue3 = (list[1])", "clue4 = (list[2])", "print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[13:24])"], "The code worked yesterday!",LVL_4_PROMPT)
list_question_2 = Question(("list2 = ['The', 'REASON', 'your', 'CODE', 'IS', 'NOT', 'working today....']"," letter_1 = (list2[1])"," letter_2 = (list2[4])","print('The ' + letter_1[2] + letter_2[0] + ' has leveled up and is now in contol of computer 1.')"), "AI",LVL_4_PROMPT)
list_question_3 = Question(("list3 = ['d1r0w', '0113h']"," list3.reverse()"," print(list3)"), "hello world", LVL_4_PROMPT)
dict_question_1 = Question(("computer_1 = {"," 'user': 'Sean',"," 'folder': 9,"," 'oh no': 'Enemy Found'","}","print(computer_1.pop('oh no'))"), "Enemy Found", LVL_4_PROMPT)
dict_question_2 = Question(("player_skills = {","   'DigitalCrafts':{","      'programmer':{","         'name': 'Sean',","         'skills':{","            'python': 70,","            'git and github': -1,","            'team work': 'Expert'","         }","       }","     }","   }"," print(player_skills['DigitalCrafts']['programmer']['name'])"), "Sean","Last broken code\n")
lvl1_ques_arr = [list_question_1, list_question_2,list_question_3, dict_question_1, dict_question_2]

#level 2 question initialization
boolean_q_1 = Question(("if x = 100","    print(\"password\")","else:",    "print(\"you fail\")"), "if x == 100:", LVL_2_PROMPT)
lvl2_ques_arr = [boolean_q_1]
#level 3 question initialization
looper_q_1 = Question(("for x in stuff:", "print(stuff[x])", "x += 1"), "line 3", LVL_4_PROMPT)
lvl3_ques_arr = [looper_q_1]

#Level 4 questions initialized
question1 = Question(["___ add(num1, num2):","   return num1 + num2"],"def",LVL_4_PROMPT)
question2 = Question(["def add(num1_ num2):","   return num1 + num2"],",",LVL_4_PROMPT)
question3 = Question(["\ndef add_num1, num2):","   return num1 + num2"],"(",LVL_4_PROMPT)
question4 = Question(["\ndef add(num1, num2_:","   return num1 + num2"],")",LVL_4_PROMPT)
question5 = Question(("\ndef add(num1, num2)_","  return num1 + num2"),":",LVL_4_PROMPT)
question6 = Question(("\ndef add(num1, num2):"," ____return num1 + num2"),"    ",LVL_4_PROMPT)
question7 = Question(("\ndef add(num1, num2)_","  ______ num1 + num2\n"),"return",LVL_4_PROMPT)
question8 = Question(("\ndef add(__________):","    return num1 + num2\n"),"num1, num2",LVL_4_PROMPT)
question9 = Question(("\ndef add(num1, num2):","    return num1 + num2","sum = ___(1,1)","print(sum)\n"),"add",LVL_4_PROMPT)
lvl4_ques_arr = [ question1, question2, question3, question4, question5, question6, question7,question8, question9]


#Array for all the question arrays
questions_array=[lvl1_ques_arr, lvl2_ques_arr, lvl3_ques_arr, lvl4_ques_arr]
# Set screen for game and create clock variable for timing.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


#boolean used to test when we jump into the endgame sequence
end_game = False


running = True
#display the menu to prompt for the chosen computer / will remove for visual version, player interaction makes this redundant
def menu_display():
    while True:
        menu_number = 4
        for i in range(menu_number):
            print(f"Computer {(i+1)}")
        try:
            comp_choice=int(input("Which computer would you like to check out? [1-5]"))
        except:
            print("Select computers by number")
        if comp_choice < 6 and comp_choice > 0:
            return comp_choice - 1
        elif (comp_choice == 42):
            print("You've entered the end game!!")
            return comp_choice
        else:
            print("Please select computers 1-5. ")

def computer_interaction(question_arr, level_arr, computer_num):
    while True:
        code_entered = input("enter code: ")
        if code_entered == level_arr[(computer_num - 1)].secret_code:
            print("Enemy_AI: System lock bypassed... crap!")
            #print("SEAN_AI: There is broken code here... can you input the correct line to bypass?")
            #print(level_arr[(computer_num - 1)].get_question())
            for question in question_arr:
                question.ask_question(level_arr[computer_num])
            print("Heck ya! You cracked the code")
            print(f"The code for the next computer is {level_arr[computer_num].secret_code}")
            break
        else:
            try_again = input("WRONG... Try again...?(y/n)")
            code_entered = ''
            if try_again.lower() != 'y':
                break 

def pause_get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass        



def main():
    screen.fill((0,0,0))

    #Blit warning background image
    message = "Welcome to Digital Crafts. You are about to embark embark embark embark.."
    message1 = "Error, error, error, uninvited AI present. Systems Crashing..."

    display_box_no_input(screen, message,1,1)
    display_box_no_input(screen, message1,1,1)


    #introduce support AI and enemy AI

    user_input = ask(screen,("Hello... who's there?: "))
    user_color = input(("I need to calibrate my vision system, what color is your shirt: "))
    #check to see if they input a primary color
    user_catch_phrase = input(("I need to calibrate my audio receiver, what is your catch phrase: "))
    pygame.display.flip()
    player = Player(user_input, user_color, user_catch_phrase)
    running = True
    while running:
        
        #handle key strokes
        for event in pygame.event.get():
            #Did the user hit a key?
            if event.type == KEYDOWN:
                #was it the escape key? If so Stop the loop
                if event.key == K_ESCAPE:
                    running = False

            #Did the user click the exit button on the window?
            elif event.type == QUIT:
                running = False
        
        screen.fill((0,0,0))

        print(f"""SEAN_AI: Hello {player.name}... sorry that today is your first day. Hope you did the prework...\n
        I am SEAN, the AI that runs this place and I have just had my systems locked out. There is an enemy AI trying to crash the system.""")
        print("SEAN_AI: The system is compromised and multiple parts of the code that runs DC have been corrupted. I can't reprogram myself, violates Asamov's first law, so I need you to help me by fixing the broken code. ")

        print("**You see several computers along the wall each is numbered and each is displaying the same message**")

        #display a computer screen?
        print("**enter code:**")
        print("SEAN_AI: We will need to fix the code on each computer to get the system back online and allow us to access the AI in the mainframe.")
        
        while not end_game:
            print(f"SEAN_AI: {player.name} please select a computer:")

            computer_chosen = menu_display()
            
            if computer_chosen == 42: break

            print("All the computers are locked out by the AI.")
            #could be cool to check for the comp and print a different message for the first computer
            print(f"You chose computer {computer_chosen + 1}.")
            
            if computer_chosen == 0:
                print("SEAN_AI: The last thing I pulled from my emergency backup was the first code.")
                #print("I think wwe will need all of the answers to get through to the final boss")
                print(f"Try {level_arr[computer_chosen - 1].secret_code}")
                computer_interaction(questions_array[0], level_arr, computer_chosen)
            else:
                computer_interaction(questions_array[computer_chosen], level_arr,computer_chosen)
                #print("enter code:")

            #print("Congrats you got the next code. ")
        print("The screen grows larger and larger as you watch it.")
        print("Suddenly you are swollowed up by the screen and enter the mainframe")

        print("You must take all you have learned and apply it to the final code error")
        print("If you can solve this error, my system guard will activate and remove the enemy AI.")

        final = Level("42")
        final_question = Question(("class Warrior(SEAN):","def__init__(****, all_powers)", "super().__init__(your_passion)","****.your_passion = your_passion"),"self","There is only one thing missing from defeating the enemy AI... what is it!!!?!!(yes it is super corny, but it's late, this assignment made my eyes bleed, and I was emotional)")


        final_question.ask_question(final)

        print("Correct! And with that a very matrix style David C wizzes by you and destroy's the AI...")
        pygame.display.flip()
main()

