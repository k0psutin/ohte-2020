import pygame
from pygame.constants import MOUSEBUTTONDOWN


class Button():

    def __init__(self,
                 text,
                 size_x,
                 size_y,
                 offset_x,
                 offset_y,
                 font,
                 display,
                 action=None,
                 action_value=None):

        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        self.font = font
        self.display = display

        self.width = display.get_width()
        self.height = display.get_height()

        self.size_x = size_x
        self.size_y = size_y

        self.action = action
        self.action_value = action_value

        self.button_pos_x = (self.width/2-(size_x/2))+(self.width*offset_x)
        self.button_pos_y = (self.height/2-(size_y/2))+(self.height*offset_y)

        self.x_limit = self.button_pos_x + self.size_x
        self.y_limit = self.button_pos_y + self.size_y

        self.text_pos_x = (self.width/2)+(self.width*offset_x)
        self.text_pos_y = (self.height/2)+(self.height*offset_y)

        self.button_text = self.font.render(text, True, self.color_light)
        self.button_active_text = self.font.render(text, True, self.color_dark)
        self.button_text_position = self.button_text.get_rect()
        self.button_text_position.center = (self.text_pos_x, self.text_pos_y)

        self.button_pos = (self.button_pos_x, self.button_pos_y)

        self.clicked = False

    def change_button_color(self, color, button_text):
        pygame.draw.rect(self.display, color, [
            self.button_pos_x, self.button_pos_y,
            self.size_x, self.size_y])
        self.display.blit(button_text, self.button_text_position)

    def change_button_text(self, text):
        self.button_text = self.font.render(text, True, self.color_light)

    def update(self, event=None, stay_down=False):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        if self.button_pos_x <= mouse_pos_x <= self.x_limit and \
                self.button_pos_y <= mouse_pos_y <= self.y_limit and \
                self.action is not None:
            self.change_button_color(self.color_light, self.button_active_text)
            self.display.blit(self.button_active_text,
                              self.button_text_position)

        else:
            if stay_down is True:
                self.change_button_color(
                    self.color_light, self.button_active_text)
                self.display.blit(self.button_active_text,
                                  self.button_text_position)
            else:
                self.change_button_color(self.color_dark, self.button_text)
                self.display.blit(self.button_text,
                                  self.button_text_position)

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x_pos, y_pos = event.pos

            if self.button_pos_x <= x_pos <= self.x_limit and \
                    self.button_pos_y <= y_pos <= self.y_limit:
                if self.action is not None:
                    if self.action_value is not None:
                        self.action(self.action_value)
                    else:
                        self.action()
