import pygame
import math

#Intialize Pygame
pygame.init()

#Create the screen W,H
screen = pygame.display.set_mode((800,600))
screenImg = pygame.image.load("Game_Board.png").convert()
    

#Title and Icon 
pygame.display.set_caption("Game Name")

#Player
playerImg = pygame.image.load("Sean_Front.png").convert_alpha()
playerX = 175
playerY = 345
playerX_change = 0
playerY_change = 0


def player(x,y):
    #Drawing image to screen
    screen.blit(playerImg,(x,y))

#computer
computerImg = pygame.image.load('laptop.png')

compx = [72,400,80,650]
compy = [113,400,368,400]
def computer ():
    screen.blit(computerImg,(compx[0],compy[0]))
    screen.blit(computerImg,(compx[1],compy[1]))
    screen.blit(computerImg,(compx[2],compy[2]))
    screen.blit(computerImg,(compx[3],compy[3]))
    
#Game Loop
running = True
while running:

    screen.blit(screenImg,(0,0))

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
                playerImg = pygame.image.load("Sean_Float_Up_Alt.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

            if event.key == pygame.K_DOWN:
                playerImg = pygame.image.load("Sean_Front.png").convert_alpha()
                playerX_change = 0
                playerY_change = 0

    # Drawing the player on the screen with a boundary
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

    #fuction to call computer
    computer()
    #function to display player
    player(playerX,playerY)
    pygame.display.update() 