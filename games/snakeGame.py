# Snake Game!

import pygame  # all the necessary for 2D game, sound and etc
import sys  # has exist
import random  # random positioned food for snake
import time  # for sleeping in the end or on error

checkErrors = pygame.init()  # initializing pygame
if checkErrors[1] > 0:  # (6,0) tuple, we check if there is any errors
    print("(!) Had {0} initializing errors, "
          "exiting...".format(checkErrors[1]))
    sys.exit(-1)  # exiting system
else:
    print("(+) PyGame successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))  # Creating player surface
pygame.display.set_caption("Snake Game!")  # Creating title for player surface

# Colors
red = pygame.Color(255, 0, 0)  # game over  # R-red,G-green,B-blue
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS = Frames Per Second
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]  # [x,y] coordinates
snakeBody = [[100, 50], [90, 50], [80, 50]]  # snake body with list of lists

# Food position randomly
foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]  # [x,y] coordinates randomly
foodSpawn = True

direction = "RIGHT"
changeTo = direction

score = 0
ticksPerSecond = 20

# Game over function
def gameOver():
    myFont = pygame.font.SysFont("monaco", 72)
    goSurf = myFont.render("Game Over!", True, red)
    goRect = goSurf.get_rect()
    goRect.midtop = (360, 15)
    playSurface.blit(goSurf, goRect)
    showScore(0)
    pygame.display.flip()  # to show smth on screan
    time.sleep(4)
    pygame.quit()  # for pygame to exit
    sys.exit()  # for console / game to exit

def showScore(choice=1):
    sFont = pygame.font.SysFont("monaco", 24)
    sSurf = sFont.render("Score : {0}".format(score), True, black)
    sRect = sSurf.get_rect()
    if choice == 1:
        sRect.midtop = (80,10)
    else:
        sRect.midtop = (360, 120)
    playSurface.blit(sSurf, sRect)

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(quit()))

    # Validation of direction
    if changeTo == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeTo == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeTo == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeTo == "DOWN" and not direction == "UP":
        direction = "DOWN"

    # increasing x,y values of snake movement
    if direction == "RIGHT":
        snakePos[0] += 10
    if direction == "LEFT":
        snakePos[0] -= 10
    if direction == "UP":
        snakePos[1] -= 10
    if direction == "DOWN":
        snakePos[1] += 10

    # Snake body mechanism and food eating growing
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:  # true then grow
        score += 1
        ticksPerSecond +=0.4
        foodSpawn = False  # ate a food and not spawn now
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]  # [x,y] coordinates randomly
    foodSpawn = True

    playSurface.fill(white)  # fill() means to fill entire screen with given color & without .flip() wont work
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 700 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 440 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0]== block[0] and snakePos[1]== block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(ticksPerSecond) #tick() means how many ticks per second


#pyinstaller - galima executable padaryti