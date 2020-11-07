import pygame
import os


class GameCard():

    def __init__(self,
                 card,
                 size_x,
                 size_y,
                 offset_x,
                 offset_y,
                 display,
                 font):

        self.rank = card.get_rank_type()

        self.suit = card.get_suit_type()

        self.suit_color = card.get_color_code()
        self.color = (0, 0, 0)

        path = os.path.join('src', 'sprites', card.get_suit_type())

        self.display = display

        self.width = display.get_width()
        self.height = display.get_height()
        self.font = font

        self.size_x = size_x
        self.size_y = size_y
        self.card_pos_x = (self.width/2-(size_x/2))+(self.width*offset_x)
        self.card_pos_y = (self.height/2-(size_y/2))+(self.height*offset_y)

        self.x_limit = self.card_pos_x + self.size_x
        self.y_limit = self.card_pos_y + self.size_y

        self.card_pos_x = (self.width/2)+(self.width*offset_x)
        self.card_pos_y = (self.height/2)+(self.height*offset_y)

        self.card_rank_left = self.font.render(
            self.rank, True, self.suit_color)
        self.card_rank_position_left = self.card_rank_left.get_rect()
        self.card_rank_position_left.center = (
            self.card_pos_x+(0.0208*self.width),
            self.card_pos_y+(0.033*self.height))

        self.card_rank_right = self.font.render(
            self.rank, True, self.suit_color)
        self.card_rank_position_right = self.card_rank_right.get_rect()
        self.card_rank_position_right.center = (
            self.card_pos_x+(0.118056*self.width),
            self.card_pos_y+(0.3 * self.height))

        self.card_suit = pygame.image.load(path).convert_alpha()

        self.card_suit_position = self.card_suit.get_rect()
        self.card_suit_position.center = (
            self.card_pos_x+(0.07*self.width),
            self.card_pos_y+(0.167*self.height))

    def update(self):
        self.display.blit(self.card_rank_left,
                          self.card_rank_position_left)
        self.display.blit(self.card_rank_right,
                          self.card_rank_position_right)
        self.display.blit(self.card_suit,
                          self.card_suit_position)
        pygame.draw.rect(self.display, self.color, [
            self.card_pos_x, self.card_pos_y,
            self.size_x, self.size_y], 1)
