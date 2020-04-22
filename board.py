import pygame
import random
from settings import *



class Board:
      def __init__(self, screen, start_pos, color):
            self.screen = screen
            self.color = color
            self.speed = BOARD_SPEED
            self.direction = 0
            self.x = start_pos[0]
            self.y = start_pos[1]
            self.start_pos = start_pos
            


      def show(self, size_x, size_y):
            """ drawing board on screen

            """
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, size_x, size_y))


      def move(self):
            """ change self.x and self.y of
            board

            """
            if self.y < 0 and self.direction == -1:
                  self.direction = 0
            elif self.y > SCREEN_SIZE[1] - BOARD_SIZE_Y and self.direction == 1:
                  self.direction = 0
            else:
                  self.y += self.speed * self.direction

      def take_start_pos(self):
            self.x = self.start_pos[0]
            self.y = self.start_pos[1]
                  

class ComputerBoard(Board):
      def __init__(self, screen, start_pos, color, cube):
            super().__init__(screen, start_pos, color)
            self.x += SCREEN_SIZE[0] - BOARD_SIZE_X

      def move(self, cube_y):
            if self.y + BOARD_SIZE_Y // 2 > cube_y - CUBE_SIZE:
                  self.direction = -1
            if self.y + BOARD_SIZE_Y // 2 <= cube_y + CUBE_SIZE:
                  self.direction = 1
            if self.y < 0 and self.direction == -1:
                  self.direction = 1
            if self.y > SCREEN_SIZE[1] - BOARD_SIZE_Y and self.direction == 1:
                  self.direction = -1

            self.y += self.speed * self.direction

      def take_start_pos(self):
            self.x = self.start_pos[0] + SCREEN_SIZE[0] - BOARD_SIZE_X
            self.y = self.start_pos[1]
      
                  
            
            
