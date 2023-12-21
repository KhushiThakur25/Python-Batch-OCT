import pygame
pygame.init()
screenWidth = 1000
screenHeight = 500
size = screenWidth,screenHeight
screen = pygame.display.set_mode(size)

red = 255,0,0
white = 255,255,255
move_x = 0.3
move_y = 0.3
x,y,w,h = 0,0,50,50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(red)
    pygame.draw.rect(screen,white,[x,y,w,h])
    x += move_x
    y += move_y
    if x > screenWidth-w:
        move_x -= 0.3
    elif x < 0:
        move_x = 0.3
    if y > screenHeight-h:
        move_y -= 0.3
    elif y < 0:
        move_y = 0.3
    
   
   # pygame.draw.circle(screen,white,[200,100],60)
    pygame.display.flip()
