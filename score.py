import pygame
from settings import *


class Score:
      def __init__(self):
            self.comp_score = 0
            self.you_score = 0

      def add_comp_score(self):
            if self.comp_score < 10:
                  self.comp_score += 1
                  return False
            return True

      def add_you_score(self):
            if self.you_score < 10:
                  self.you_score += 1
                  return False
            return True

      def show(self, screen):
            scores = f'You {self.you_score}:{self.comp_score} Computer'
            font = pygame.font.Font(SCORE_FONT, SCORE_FONT_SIZE)
            text = font.render(scores, True, WHITE)
            screen.blit(text, SCORE_POS)

