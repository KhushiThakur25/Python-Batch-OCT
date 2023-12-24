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

frogX = random.randint(1,screenWidth-frogWidth)
frogY = random.randint(1,screenHeight-frogHeight)
red = 255,0,0
white = 255,255,255

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])
move_x = 0.3
move_y = 0.3
speed = 1
x,y,w,h = 0,0,50,50

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
   
   # pygame.draw.circle(screen,white,[200,100],60)
    pygame.display.flip()
