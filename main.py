import pygame
import sys
from settings import *
from game import Game




def main():
      pygame.init()
      screen = pygame.display.set_mode(SCREEN_SIZE)
      pygame.display.set_caption(NAME_GAME)
      clock = pygame.time.Clock()
      game = Game(screen)
      while True:
            clock.tick(FPS)
            if game.play:
                  game.game_event()
                  game.screen_update()
            else:
                  pass


if __name__ == "__main__":
      main()
            
      
      


