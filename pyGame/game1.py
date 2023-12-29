import pygame
import random
pygame.init()
screenWidth = 1000
screenHeight = 500
size = screenWidth,screenHeight
screen = pygame.display.set_mode(size)
bg = pygame.image.load('bgg.png')
frogImg = pygame.image.load('fg1.png')

frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()


red = 255,0,0
white = 255,255,255
yellow = 255,255,0
w,h = 50,50

def homeScreen():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Welcome to the Jungle", True,white)
    
    font_2 = pygame.font.SysFont(None,70)
    text_2 = font_2.render("Press SPACE to start Game..", True,white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(bg,(0,0))
        screen.blit(text,(100,100))
        screen.blit(text_2,(50,300))
        pygame.display.update()


def gameOver():
    font = pygame.font.SysFont(None,200)
    text = font.render("Game Over..", True, yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text,(100,100))
        pygame.display.update()

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])

def score(counter):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(counter),True,yellow)
    screen.blit(text,(100,10))

def game():
    move_x = 0.3
    move_y = 0.3
    speed = 2
    counter = 0
    x,y = 0,0
    frogX = random.randint(1,screenWidth-frogWidth)
    frogY = random.randint(1,screenHeight-frogHeight)
    FPS = 2500
    clock = pygame.time.Clock()
    snakeLength = 1
    snakeList = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = speed
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -speed
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = speed
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -speed
                    move_x = 0
                
            else:
                move_x = 0
                move_y = 0
    # screen.fill(red)
    
        screen.blit(bg,(0,0))
        screen.blit(frogImg,(frogX,frogY))
        frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
        snakeRect = pygame.draw.rect(screen,white,[x,y,w,h])
        x += move_x
        y += move_y
        score(counter)

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        drawSnake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        if x > screenWidth:
        # move_x -= 0.3
            x = -w
        elif x < -50:
        # move_x = 0.3
            x = screenWidth
        if y > screenHeight:
        # move_y -= 0.3
            y = -h
        elif y < -50:
        # move_y = 0.3
            y = screenHeight
        if frogRect.colliderect(snakeRect):
            frogX = random.randint(1,screenWidth-frogWidth)
            frogY = random.randint(1,screenHeight-frogHeight)
            snakeLength += 40
            FPS += 50
            counter += 1
        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()
   
   # pygame.draw.circle(screen,white,[200,100],60)
        pygame.display.flip()
        clock.tick(FPS)
homeScreen()