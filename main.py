import pygame
import sys
from settings import *
from board import Board, ComputerBoard
from cube import Cube


def game_event(you, comp, cube):
      """
      processing all events of game like quit, pressing key
      on keyboard etc

      """
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  sys.exit()

            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_DOWN:
                        you.direction = 1
                  if event.key == pygame.K_UP:
                        you.direction = -1
            if event.type == pygame.KEYUP:
                  if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        you.direction = 0
            if event.type == pygame.MOUSEMOTION:
                  if you.y - event.pos[1] >= 0:
                        you.direction = -1
                  elif you.y - event.pos[1] <= -1 * BOARD_SIZE_Y:
                        you.direction = 1
                  else:
                        you.direction = 0
      you.move()
      cube.move(you.y, comp.y)
      comp.move(cube.y)
      


def screen_update(screen, you, comp, cube):
      """ show all elements of game
      
      """
      screen.fill(BLACK)
      #pygame.draw.rect(screen, WHITE, (0, 0, S_BOARD_X, SIZE))
      you.show(BOARD_SIZE_X, BOARD_SIZE_Y)
      comp.show(BOARD_SIZE_X, BOARD_SIZE_Y)
      cube.show(CUBE_SIZE, CUBE_SIZE)
      pygame.display.update()


def main():
      pygame.init()
      screen = pygame.display.set_mode(SCREEN_SIZE)
      pygame.display.set_caption(NAME_GAME)
      clock = pygame.time.Clock()
      you = Board(screen, BOARD_START_POS, RED)
      cube = Cube(screen, CUBE_START_POS, RED)
      comp = ComputerBoard(screen, BOARD_START_POS, RED, cube)
      while True:
            clock.tick(FPS)
            game_event(you, comp, cube)
            screen_update(screen, you, comp, cube)


if __name__ == "__main__":
      main()
            
      
      


