import pygame
import sys
import random


pygame.init()
width = 400; heigth = 400
screen = pygame.display.set_mode((width,heigth))

pygame.display.set_caption("puzzles")
def draw_grid():
    row = col = 5
    row_width = width // row
    col_heigth = heigth // col
    x = y = 0
    for i in range (1,row):
        x += row_width

        pygame.draw.line(screen,pygame.Color("white"),(x,0),(x,heigth))
    for i in range(1,col):
        y += col_heigth
        pygame.draw.line(screen,pygame.Color("white"),(0,y),(width,y))
def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    while True:
        draw_grid()
        screen.fill(pygame.Color("pink"))
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
main()
