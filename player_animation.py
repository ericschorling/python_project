import pygame
import random
import math
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
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#computer
computerImg = pygame.image.load('laptop.png')


def computer ():
    screen.blit(computerImg,(100,100))
    screen.blit(computerImg,(400,400))
    screen.blit(computerImg,(100,400))
    screen.blit(computerImg,(400,100))
    screen.blit(computerImg,(700,100))
    screen.blit(computerImg,(700,400))


def player(x,y):
    #Drawing image to screen
    screen.blit(playerImg,(x,y))

#Game Loop
running = True
while running:
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
   
    #function to display computer
    computer()
    #function to display plaer
    player(playerX,playerY)
    pygame.display.update()