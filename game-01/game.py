import pygame
from pygame.locals import *
pygame.init()

# canvas setup
x = 800
y = 600
concrete_color = (100,100,100)

# object setup
car = pygame.image.load('./img/yellow-car-01.png')
car_width = 85
car_height = 170
speed = 10
obj_x = x/2 - car_width/2
obj_y = y/2 - car_height/2
#obj_radious = 10
#obj_color = (255, 255, 0)

# grass setup
grass_x = x/4
grass_color = (0,100,0)

# border setup
border_width = 20
border_color = (0,0,150)

# line setup
line_width = 8
line_color = (200, 255, 0)


window = pygame.display.set_mode((x,y))
pygame.display.set_caption('Game 01')

open_window = True

while open_window:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    commands = pygame.key.get_pressed()
#    if commands[pygame.K_UP] and obj_y > 0:
#        obj_y -= speed
#    if commands[pygame.K_DOWN] and obj_y < y - car_height:
#        obj_y += speed
    if commands[pygame.K_LEFT] and obj_x > grass_x + border_width:
        obj_x -= speed
    if commands[pygame.K_RIGHT] and obj_x < x - grass_x - border_width - car_width:
        obj_x += speed

    # CONCRETE
    window.fill(concrete_color)
    # LEFT GRASS
    pygame.draw.rect(window, grass_color, (0, 0, grass_x, y))
    # RIGHT GRASS
    pygame.draw.rect(window, grass_color, (x-grass_x, 0, grass_x, y))
    # LEFT BORDER
    pygame.draw.rect(window, border_color, (grass_x, 0, border_width, y))
    # RIGHT BORDER
    pygame.draw.rect(window, border_color, (x - grass_x - border_width, 0, border_width, y))
    # LEFT LINE
    pygame.draw.rect(window, line_color, (x/2 - line_width * 2, 0, line_width, y))
    # RIGHT LINE
    pygame.draw.rect(window, line_color, (x/2 + line_width * 2, 0, line_width, y))
    # CAR
    window.blit(car, (obj_x, obj_y))
    #pygame.draw.circle(window, obj_color, (obj_x, obj_y), obj_radious*2)
    pygame.display.update()
    

pygame.quit()