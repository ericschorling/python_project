#This will be the main game file.
#class level that will be the parent for all the levels 
import random
from pp_classes import Level
from pp_classes import Player
from pp_classes import Level2
from test2 import Question

QUESTION_1= "SEAN_AI: Need to fix this print statement:\nprint('destroy all humans'"
#ANSWER_PROMPT = "Tell me your answer"
# questions initialized
level1= Level(QUESTION_1, "print('destroy all humans')","x = 2 + n + 4 -5")
lvl2 = Level2("","","","Arrrg")
lvl3 = Level("","","hey it's secret")
level_arr = [level1,lvl2,lvl3]

LVL_6_PROMPT = 'Fill in the blank\n'

question1 = Question("\n___ add(num1, num2):\n   return num1 + num2\n","def",LVL_6_PROMPT)
question2 = Question("\ndef add(num1_ num2):\n   return num1 + num2\n",",",LVL_6_PROMPT)
question3 = Question("\ndef add_num1, num2):\n   return num1 + num2\n","(",LVL_6_PROMPT)
question4 = Question("\ndef add(num1, num2_:\n   return num1 + num2\n",")",LVL_6_PROMPT)
question5 = Question("\ndef add(num1, num2)_\n  return num1 + num2\n",":",LVL_6_PROMPT)
question6 = Question("\ndef add(num1, num2):\n ____return num1 + num2\n","    ",LVL_6_PROMPT)
question7 = Question("\ndef add(num1, num2)_\n  ______ num1 + num2\n","return",LVL_6_PROMPT)
question8 = Question("\ndef add(__________):\n    return num1 + num2\n","num1, num2",LVL_6_PROMPT)
question9 = Question("\ndef add(num1, num2):\n    return num1 + num2\n\nsum = ___(1,1)\nprint(sum)\n","add",LVL_6_PROMPT)

list_question_1 = Question("\nlist = ['The cat knows code', 'She worked as a Project Manager before attending DigitalCrafts', 'Today is not yesterday!']\n clue1 = (list[0])\n clue2 = (list[0])\n clue3 = (list[1])\n clue4 = (list[2])\n print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[13:24])", "The code worked yesterday!",LVL_6_PROMPT)
#question array for level 6
question_array = [list_question_1, question1, question2, question3, question4, question5, question6, question7,question8, question9]
end_game = False

print(level1.get_question())
running = True
#display the menu to prompt for the chosen computer
def menu_display():
    while True:
        menu_number = 5
        for i in range(menu_number):
            print(f"Computer {(i+1)}")
        try:
            comp_choice=int(input("Which computer would you like to check out? [1-5]"))
        except:
            print("Select computers by number")
        if comp_choice < 6 and comp_choice > 0:
            return comp_choice
        elif (comp_choice == 47):
            print("You've entered the end game!!")
        else:
            print("Please select computers 1-5. ")

def computer_interaction(question_arr, level_arr, computer_num):
    code_entered = input("enter code")

    if code_entered == level_arr[(computer_num - 2)].secret_code:
        print("Enemy_AI: System lock bypassed... crap!")
        #print("SEAN_AI: There is broken code here... can you input the correct line to bypass?")
        #print(level_arr[(computer_num - 1)].get_question())
        for question in question_arr:
            question.ask_question()

        #while True:
        #   player_answer = input("Enter the corrected line of code to fix the program and decrypt the code.")
        #   if player_answer == level_arr[(computer_num - 1)].answer:
        #     print("SEAN_AI: Boom, you got it")
        #     print("ENEMY_AI: Crap you foiled me with your programming wizardry.")
        #      fix the comp_chosen so it doesn't keep reducing by 1, that's dumb
            #    print(level_arr[(computer_chosen - 1)].secret_code)
                #add option to push this to the notebook array.
             #   break
            #else:
             #   print("That code didn't seem to fix the problem")
              #  replay = input("Try again? (y/n)")
               # if replay.lower() != 'y':
                #    break

print("Welcome to Digital Crafts. You are about to embark embark embark embark..")
print("Error, error, error, uninvited AI present. Systems Crashing...")

#introduce support AI and enemy AI

user_input = input(("Hello... who are you: "))
user_color = input(("I need to calibrate my vision system, what color is your shirt: "))
#check to see if they input a primary color
user_catch_phrase = input(("I need to calibrate my audio receiver, what is your catch phrase: "))

player = Player(user_input, user_color, user_catch_phrase)

while running:
    
    print("""Hello digital crafter... sorry that today is your first day. Hope you did the prework...\n
            I am SEAN, the AI that runs this place and I have just had my systems locked out. There is an enemy AI trying to crash the system.""")
    print("SEAN_AI: The system is compromised and multiple parts of the code that run DC have been corrupted. I can't reprogram myself, violates Asamov's first law, so I need you to help me by fixing the broken code. ")

    print("**You see several computers along the wall each is numbered and each is displaying the same message**")

    #display a computer screen?
    print("**enter code:**")
    print("SEAN_AI: We will need to fix the code on each computer to get me back online and allow us to access the AI in the mainframe.")
    
    while not end_game:
        print(f"SEAN_AI: {player.name} please select a computer:")

        computer_chosen = menu_display()
        
        print("All the computers are locked out by the AI.")
        #could be cool to check for the comp and print a different message for the first computer
        print(f"You chose computer {computer_chosen}.")
        
        if computer_chosen == 1:
            print("SEAN_AI: The last thing I pulled from my data banks was the first code.")
            print("I think wwe will need all of the answers to get through to the final boss")
            print("Try \"d1r0w 0ll3h\"")
            computer_interaction(question_array, level_arr, computer_chosen)
        else:
            computer_interaction(question_array, level_arr,computer_chosen)
            #print("enter code:")

        print("Congrats you got the next code. ")






#question1.ask_question()
#question2.ask_question()
#question3.ask_question()
#question4.ask_question()
#question5.ask_question()
#question6.ask_question()
#question7.ask_question()
#question8.ask_question()
#question9.ask_question()


