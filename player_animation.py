
import pygame
import random
import math
import os
from python_project_main import Message_Box
from python_project_main import message_display
from python_project_main import level_arr
from python_project_main import questions_array
from python_project_main import pause_get_key
from python_project_main import ask
from python_project_main import game_intro
#from python_project_main import look_for_down
#from python_project_main import pause_get_mouse
#Intialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

#pygame.mixer.music.load("2015-09-25_-_Old_Video_Game_Music_1_-_David_Fesliyan.wav")
#pygame.mixer.music.play(loops=-1)
#Create the screen W,H
screen = pygame.display.set_mode((800,600))
screenImg = pygame.image.load("Game_Board.png").convert()
narration_box = Message_Box(20, 470, 70 )    
#Background 
# background = pygame.image.load('bg.jpg')
#Title and Icon 
pygame.display.set_caption("Sean vs AI!")

#Player
playerImg = pygame.image.load("Sean_Front.png").convert_alpha()
computer_screen_Img = pygame.image.load("computer_screen.png")
global playerX
playerX = 175
global playerY 
playerY= 345
playerX_change = 0
playerY_change = 0
BLACK_BACKGROUND = (0,0,0)
#computer change to have a number for each one
computerImg = pygame.image.load('laptop.png')
computerImg_Comp = pygame.image.load('Computer_Completed.png')
bossImg = pygame.image.load('Final_Computer.png')
#computer flag
c1 = 0
c2 = 0
c3 = 0 
c4 = 0
c5 = 0

#remove
def button(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # #Takes width, height and location(x,y)
    while True:
        #if 357+122 > mouse[0] > 357 and 480+33 > mouse[1] > 480:
        if click[0] == 1:
            print(mouse)
            break

compx = [72,80,400,650,400]
compy = [113,368,368,368,108]
def computer (end_game):
    
    if c1 != 1 : screen.blit(computerImg,(compx[0],compy[0])) | screen.blit(computerImg_Comp,(compx[0],compy[0]))  
    screen.blit(computerImg,(compx[1],compy[1]))
    screen.blit(computerImg,(compx[2],compy[2]))
    screen.blit(computerImg,(compx[3],compy[3]))
    #add endgame computer image only when endgame is triggered.
    if end_game: screen.blit(bossImg,(compx[4],compy[4]))

def player(x,y):
    #Drawing image to screen
    screen.blit(playerImg,(x,y))

font = pygame.font.Font('freesansbold.ttf',18)
def show_text(x,y):
    text = font.render("Enter Secret Code to Unlock Computer ",True,(255,255,255))
    screen.blit(text,(x,y))
    #pause_get_key()


def iscollision(alienX, alienY, bulletX, bulletY):
        #distance between two coordinates
        distance = math.sqrt(math.pow(alienX-bulletX,2)+math.pow(alienY-bulletY,2))
        if distance < 40:
            return True 
        else:
            return False

#Game Loop
running = True
end_game = False
game_over = False
first_run = True
flag = 0 #DON"T EVER CHANGE THIS


introImg = pygame.image.load("Game_Opening_Screen.png").convert()
screen.blit(introImg,(0,0))
narration_box.message_display([""])
#game_intro()
pause_get_key()
#button(357,480,122,33)

while running:
    #os.system("aplay 2015-09-25_-_Old_Video_Game_Music_1_-_David_Fesliyan.wav&")

    

    if flag != 1:
        #Background Color (RGB Values)
        screen.blit(screenImg,(0,0))
        #screen.fill((44,2,38))

    #Gets events from inside the Pygame screen
    for event in pygame.event.get():
        #Checking if x quit button is pressed
        if event.type == pygame.QUIT:
            #Condition to exit the while loop
            running = False 
        #if a keystroke is pressed check whether right or left 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
                playerImg = pygame.image.load("Sean_Walking_Left.png").convert_alpha()
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
                playerImg = pygame.image.load("Sean_Walking_Right.png").convert_alpha()
            if event.key == pygame.K_UP:
                playerY_change = -4
                playerImg = pygame.image.load("Sean_Float_Up.png").convert_alpha()
            if event.key == pygame.K_DOWN:
                playerY_change = 4
                playerImg = pygame.image.load("Sean_Down.png").convert_alpha()

        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerImg = pygame.image.load("Sean_Walking_Right_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_LEFT:
                playerImg = pygame.image.load("Sean_Walking_Left_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_UP:
                # playerImg = pygame.image.load("Sean_Float_Up_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_DOWN:
                playerImg = pygame.image.load("Sean_Front.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0



    collision1 = iscollision(compx[0],compy[0],playerX,playerY)
    if collision1 and c1 != 1:
        c1 = 1
        #used to make it easier to c/p the different comps 
        x = 0
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            message_display([f"David_AI: I got the first code, try {level_arr[x].secret_code}"])
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, questions_array[x][questions].prompt)
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])    
        pause_get_key()

    collision2 = iscollision(compx[1],compy[1],playerX,playerY)
    if collision2 and c2 != 1:
        c2 = 1
        x = 1
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])    
        pause_get_key()

    collision3 = iscollision(compx[2],compy[2],playerX,playerY)
    if collision3 and c3 != 1:
        c3 = 1
        x = 2
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is " + level_arr[x+1].secret_code])    
        pause_get_key()

    collision4 = iscollision(compx[3],compy[3],playerX,playerY)
    if collision4 and c4 != 1:
        c4 = 1
        x = 3
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!", "Press [ENTER] to access computer"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        message_display(["You unlocked this computer!!","The next code is 42","Enemy AI Brain revealed!!"])    
        pause_get_key()
        end_game = True
    #End_game computer
    collision5 = iscollision(compx[4],compy[4],playerX,playerY)
    if collision5 and c5 != 1 and end_game:
        c5 = 1
        x = 4
        print(x)
        screen.fill(BLACK_BACKGROUND)
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        while True:
            user_input = ask(screen, "Enter Secret Code")
            if user_input == level_arr[x].secret_code:
                message_display(["CORRECT!!","For it is truly the answer to the universe", "Press [ENTER] to access the enemy AI Brain"])
                pause_get_key()
                break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        for questions in range(len(questions_array[x])):
            while True:
                message_display(questions_array[x][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[x][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    #message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        message_display(["You have defeated the evil AI and restored Digital Crafts!!"])    
        pause_get_key()
        game_over = True
    #drawing the player on the screen
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0 
    elif playerX >= 625: 
        playerX = 625
    if playerY <= 0:
        playerY = 0 
    elif playerY >= 345:
        playerY = 345
   
 


    #function to display computer and player if the player is not on the computer
    if flag != 1:
        computer(end_game)
        #function to display player
        player(playerX,playerY)
        if first_run:
            #narration_box.display_background(BLACK_BACKGROUND,300,100)
            narration_box.message_display(["Error Errror Error... Something is going wrong", "This is Digital Craft's AI David.....","If you can hear me press [ENTER]"])
            pause_get_key()
            narration_box.message_display(["I am currently under attack by an enemy AI.","Four of my databases have been compromised.","Proceed to upstairs to fix the first computer"])
            pause_get_key()
            first_run = False
    pygame.display.update()


