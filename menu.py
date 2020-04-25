import pygame
import sys
from settings import *



class Menu:
      def __init__(self, screen):
            self.screen = screen
            self.buttons = []
            self.buttons.append(ButtCont(screen, 'continue', (100, 100), 30))


      def menu_event(self):
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        for button in self.buttons:
                              return button.if_press(button.action, mouse)


      def update_screen(self):
            self.screen.fill(BLACK)
            for button in self.buttons:
                  button.draw()
            pygame.display.update()
            


class Button:
      def __init__(self, screen, text, pos, font_size):
            self.screen = screen
            self.text = text
            self.pos = pos
            self.font_size = font_size

      def draw(self):
            font = pygame.font.SysFont(None, self.font_size)
            button = font.render(self.text, True, WHITE)
            self.screen.blit(button, self.pos)

      def if_press(self, action, mouse):
            if mouse[0] > self.pos[0] and mouse[1] > self.pos[1]:
                  if mouse[0] < self.pos[0] + BUTTON_SIZE_X:
                        if mouse[1] < self.pos[1] + BUTTON_SIZE_Y:
                              return action()


class ButtCont(Button):
      def __init__(self, screen, text, pos, font_size):
            super().__init__(screen, text, pos, font_size)

      def action(self):
            return True










      
