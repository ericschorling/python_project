
import pygame
import random
import math
from python_project_main import message_display
from python_project_main import level_arr
from python_project_main import questions_array
from python_project_main import pause_get_key
from python_project_main import ask
from python_project_main import look_for_down
#Intialize Pygame
pygame.init()

#Create the screen W,H
screen = pygame.display.set_mode((800,600))

#Background 
# background = pygame.image.load('bg.jpg')
#Title and Icon 
pygame.display.set_caption("Game Name")

#Player
playerImg = pygame.image.load('hero.png')
global playerX
playerX = 370
global playerY 
playerY= 480
playerX_change = 0
playerY_change = 0

#computer
computerImg = pygame.image.load('laptop.png')
#computer flag
c1 = 0
c2 = 0
c3 = 0 
c4 = 0


compx = [100,400,100,400,700,700]
compy = [100,400,400,100,100,400]
def computer ():
    screen.blit(computerImg,(compx[0],compy[0]))
    screen.blit(computerImg,(compx[1],compy[1]))
    screen.blit(computerImg,(compx[2],compy[2]))
    screen.blit(computerImg,(compx[5],compy[5]))


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
        if distance < 27:
            return True 
        else:
            return False

#Game Loop
running = True
flag = 0
while running:
    if flag != 1:
        #Background Color (RGB Values)
        screen.fill((44,2,38))

    #Gets events from inside the Pygame screen
    for event in pygame.event.get():
        #Checking if x quit button is pressed
        if event.type == pygame.QUIT:
            #Condition to exit the while loop
            running = False 
        #if a keystroke is pressed check whether right or left 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1#speed of change
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1

        if event.type ==  pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0



    collision1 = iscollision(compx[0],compy[0],playerX,playerY)
    if collision1 and c1 != 1:
        c1 = 1
        screen.fill((0,0,0))
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        for questions in range(len(questions_array[0])):
            while True:
                message_display(questions_array[0][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[0][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
            screen.blit(pygame.image.load('computer_screen.png'),(0,0)) 
                
    collision2 = iscollision(compx[1],compy[1],playerX,playerY)
    if collision2 and c2 != 1:
        c2 = 1
        screen.fill((0,0,0))
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        for questions in range(len(questions_array[0])):
            while True:
                message_display(questions_array[0][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[0][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
    

    collision3 = iscollision(compx[2],compy[2],playerX,playerY)
    if collision3 and c3 != 1:
        c3 = 1
        screen.fill((0,0,0))
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        for questions in range(len(questions_array[0])):
            while True:
                message_display(questions_array[0][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[0][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
   

    collision4 = iscollision(compx[5],compy[5],playerX,playerY)
    if collision4 and c4 != 1:
        c4 = 1
        screen.fill((0,0,0))
        #Background Image
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
        #show_text(132,21)
        for questions in range(len(questions_array[0])):
            while True:
                message_display(questions_array[0][questions].question)
                user_input = ask(screen, "")
                if user_input == questions_array[0][questions].answer:
                    screen.blit(pygame.image.load('computer_screen.png'),(0,0))
                    message_display(["Woot Woot"])
                    break
        screen.blit(pygame.image.load('computer_screen.png'),(0,0))
    

    #drawing the player on the screen
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0#these are bondaries
    elif playerX >= 736:#Subtract 800-64, 64 is size of our hero, 800 is our window
        playerX = 736
    if playerY <= 0:
        playerY = 0#these are bondaries
    elif playerY >= 536:
        playerY = 536
   
 


    #function to display computer and player if the player is not on the computer
    if flag != 1:
        computer()
        #function to display player
        player(playerX,playerY)
    pygame.display.update()


