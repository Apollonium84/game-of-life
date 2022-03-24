import pygame
import os
import grid


os.environ["SDL_VIDEO_CENTERED"] = '1'
# Screen size settings
width, height = 1920, 1080
size = (width, height)

pygame.init()
pygame.display.set_caption("Game of life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()

pause = False
run = True

while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.john_conway(off_color=white, on_color=blue, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.handle_mouse(mouseX, mouseY)

    pygame.display.update()
pygame.quit()
