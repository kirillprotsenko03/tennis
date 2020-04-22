import pygame
import random
import sys
from settings import *
from board import Board


class Cube(Board):
      def __init__(self, screen, start_pos, color):
            super().__init__(screen, start_pos, color)
            self.__random_start()


      def __random_start(self):
            self.direction_x = CUBE_SPEED_X * random.choice([-1, 1])
            self.direction_y = CUBE_SPEED_Y * random.choice([-1, 1])

      
      def move(self, board_y, comp_board_y):
            if self.y <= 0:
                  self.direction_y *= -1
            if self.y + CUBE_SIZE >= SCREEN_SIZE[1]:
                  self.direction_y *= -1

            if self.x <= CUBE_SIZE:
                  if board_y <= self.y <= board_y + BOARD_SIZE_Y:
                        self.direction_x *= -1
                  else:
                        sys.exit()
            if self.x + CUBE_SIZE >= SCREEN_SIZE[0]:
                  if comp_board_y <= self.y <= comp_board_y + BOARD_SIZE_Y:
                        self.direction_x *= -1
            self.x += self.direction_x
            self.y += self.direction_y

