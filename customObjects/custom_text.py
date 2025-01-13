import pygame

# Copyright (C) 2025  Hohenzoler
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

class Custom_text:  # A class that generates text
    def __init__(self, display, x, y, text, font=None, font_height=50, text_color='Black', background_color=None, center=True, append=True):

        self.display = display

        self.x = x
        self.y = y
        self.font_height = font_height
        self.text = text
        self.text_color = text_color
        self.background_color = background_color
        self.append = append

        self.hidden = False

        self.center = center
        self.font = pygame.font.Font(font, self.font_height)

        self.text_to_render = self.font.render(self.text, True, self.text_color, self.background_color)
        self.rect = self.text_to_render.get_rect()

        if self.center:  # If self.center == True it sets the center of the text as self.x and self.y
            self.rect.center = (self.x, self.y)
        else:  # Else it set self.x and self.y as the top left corner of the text
            self.rect.center = (self.x + self.rect.width//2, self.y + self.rect.height//2)

        if self.append:
            self.display.objects.append(self)

    def render(self):  # Renders the text
        if not self.hidden:
            self.display.screen.blit(self.text_to_render, self.rect)

    def events(self, event):  # For now just passes when checking events
        pass

    def delete(self):
        if self.append:
            self.display.objects.remove(self)
        del self

    def update_text(self, text):
        self.text = text
        self.text_to_render = self.font.render(self.text, True, self.text_color, self.background_color)
        self.rect = self.text_to_render.get_rect()

        if self.center:  # If self.center == True it sets the center of the text as self.x and self.y
            self.rect.center = (self.x, self.y)
        else:  # Else it set self.x and self.y as the top left corner of the text
            self.rect.center = (self.x + self.rect.width // 2, self.y + self.rect.height // 2)

    def update_color(self, color, bg_color):
        self.text_color = color
        self.background_color = bg_color
