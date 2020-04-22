import pygame
import sys
import time
from settings import *
from board import Board, ComputerBoard
from cube import Cube
from score import Score



class Game:
      """ the main class in game, wich should to start game, make pause,
      count score, draw game elements.

      """
      def __init__(self, screen):
            self.screen = screen
            self.you = Board(screen, BOARD_START_POS, RED)
            self.cube = Cube(screen, CUBE_START_POS, RED)
            self.comp = ComputerBoard(screen, BOARD_START_POS, RED, self.cube)
            self.score = Score()

      def screen_update(self):
            """ show all elements of game
      
            """
            self.screen.fill(BLACK)
            self.you.show(BOARD_SIZE_X, BOARD_SIZE_Y)
            self.comp.show(BOARD_SIZE_X, BOARD_SIZE_Y)
            self.cube.show(CUBE_SIZE, CUBE_SIZE)
            pygame.display.update()
            

      def game_event(self):
            """
            processing all events of game like quit, pressing key
            on keyboard etc

            """
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        sys.exit()

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                              self.you.direction = 1
                        if event.key == pygame.K_UP:
                              self.you.direction = -1
                  if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                              self.you.direction = 0
                  if event.type == pygame.MOUSEMOTION:
                        if self.you.y - event.pos[1] >= 0:
                              self.you.direction = -1
                        elif self.you.y - event.pos[1] <= -1 * BOARD_SIZE_Y:
                              self.you.direction = 1
                        else:
                              self.you.direction = 0
            self.you.move()
            continuetion = self.cube.move(self.you.y, self.comp.y, self.score)
            self.comp.move(self.cube.y)
            if not continuetion:
                  self.cube.take_start_pos()
                  self.comp.take_start_pos()
                  self.you.take_start_pos()
                  print('you:', self.score.you_score)
                  print('comp:', self.score.comp_score)
                  time.sleep(2)
            
      
            
