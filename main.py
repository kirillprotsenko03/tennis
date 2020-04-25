import pygame
import sys
from settings import *
from game import Game
from menu import Menu




def main():
      pygame.init()
      screen = pygame.display.set_mode(SCREEN_SIZE)
      pygame.display.set_caption(NAME_GAME)
      clock = pygame.time.Clock()
      game = Game(screen)
      menu = Menu(screen)
      while True:
            clock.tick(FPS)
            if game.play:
                  game.game_event()
                  game.screen_update()
            else:
                  game.play = menu.menu_event()
                  menu.update_screen()


if __name__ == "__main__":
      main()
            
      
      


