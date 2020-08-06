import pygame
import random
import pygame.font
import pygame.event
import pygame.draw
import os
import sys
from pygame.locals import * 
# (
#     RLEACCEL,
#     K_UP,
#     K_w,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )

pygame.init()

#Define a player object by extedning pygame.sprite
#The surgace drawn on the screen is now an attribute of the player
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
#Define the enemy object
#the surface that is drwan is now an attribute of enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((20,10))
        #self.surf.fill((255,0,0))
        self.surf = pygame.image.load('missle.jpeg').convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        self.surf = pygame.image.load('asteroid.jpg').convert()
        self.surf.set_colorkey((250,250,250), RLEACCEL)
        #self.surf = pygame.Surface((32,32))
        #self.surf.fill((139,69,19))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH +20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(1,5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    #This sets the background for the text input. 
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height() / 2) - 10,
                      200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                     ((screen.get_width() / 2) - 102,
                      (screen.get_height() / 2) - 12,
                      204, 24), 1)
    #This displays the messages
    screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - (10)))
            
    pygame.display.flip()

def ask(screen, question): 
    "ask(screen, question) -> answer"
    pygame.font.init()        
    current_string = []
    display_box(screen, question + "".join(current_string))
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
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + "".join(current_string))
    return "".join(current_string)
#def a message display function for placing text on the screen
#nput("Tell me something:")

running = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
score = 0
#adding a background immage
background_image = pygame.image.load('liquid.jpeg').convert()


screen_output = ask(screen, "Solution:")


pygame.display.set_caption('Sky\'s the limit')

# Create a custom event for adding a new enemy
#events are integers, the last one that is recorded is called USEREVENT
#ADDENEMY = pygame.USEREVENT + 1
#Time is considered in milleseconds
#pygame.time.set_timer(ADDENEMY, 250)

#adding in cool asteroids that fly across the screen
ADDASTEROID = pygame.USEREVENT + 2
pygame.time.set_timer(ADDASTEROID, 1000)

#Create new player
player = Player(screen_output,"Red","Ahah" )
#
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
#enemies = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
#all_sprites.add(player)

message = f"Welcome {player.name} to the flying game.\nHopefully this will \n wrap the text."

ask(screen,message)

#def a message display function for placing text on the screen
#nput("Tell me something:")

running = True


while running:
    try:

        for event in pygame.event.get():
            #Did the user hit a key?
            if event.type == KEYDOWN:
                #was it the escape key? If so Stop the loop
                if event.key == K_ESCAPE:
                    running = False

            #Did the user click the exit button on the window?
            elif event.type == QUIT:
                running = False
            #Add a new enemy
            #elif event.type == ADDENEMY:
                #Create the new enemy and add it to the sprite groups
                #new_enemy = Enemy()
                #add it to the groups
                #enemies.add(new_enemy)
                #all_sprites.add(new_enemy)
        
            elif event.type == ADDASTEROID:
                #print("happened")
                new_asteroid = Asteroid()
                asteroids.add(new_asteroid)
                all_sprites.add(new_asteroid)
    except:       
        print("Something wrong with asteroid call...")
    #Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    #Update the player sprite based on user keypresses
    #called before so that it is behind user. 
    asteroids.update()
    player.update(pressed_keys)
    #update the enemy positions
    #enemies.update()
    
    #screen_output = ask(screen, "Name") + " was entered"
    #fills the screen with black
    screen.blit(background_image,(0,0))
    
    #this line says "draw surf onto the screen at the center"
    #define player for actual center of screen
    
    #blit player onto the screen
    #screen.blit(player.surf, player.rect)
    
    #perform location update on all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    screen.blit(player.surf, player.rect)
    #check for a collision in the game between an enemy and the player
    #if pygame.sprite.spritecollideany(player, enemies):
    #    player.kill()
    #    running = False
    #update screen
    pygame.display.flip()
    score += 1
    clock.tick(60)


    # if len(messages) != 0:
    #     x = 1
    #     for message in messages:
    #         screen.blit(fontobject.render(message, 1, (255, 255, 255)),
    #                 ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - (10*x)))
    #         x += 1
    # pygame.display.flip()   