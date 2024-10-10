import pygame
import math as Lolus

# Copyright (C) 2024  Hohenzoler
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

class Custom_image:  # A class to easier render images
    def __init__(self, display, path, x, y, w, h, append=True, loaded=True):
        self.display = display

        self.x = x  # center x of the image
        self.y = y  # center y of the image
        self.w = w  # width of the image
        self.h = h  # height of the image

        self.path = path  # path to the images

        self.loaded = loaded

        if loaded:
            self.load()

        if append:
            self.display.objects.append(self)

    def render(self):  # rendering the image at self.x , self.y
        self.display.screen.blit(self.image, (self.rect.x, self.rect.y))

    def events(self, event):
        pass

    def delete(self):
        try:
            self.display.objects.remove(self)
        except:
            pass
        del self

    def rotate_toward(self, pos):
        rel_x, rel_y = pos[0] - self.x, pos[1] - self.y

        angle = Lolus.degrees(Lolus.atan2(-rel_y, rel_x)) - 90

        self.image = pygame.transform.rotate(self.original_image, angle)

        self.update_rect()

    def update_rect(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def load(self):
        self.original_image = pygame.image.load(self.path).convert_alpha()  # loading the original image
        self.original_image = pygame.transform.scale(self.original_image,
                                                     (self.w, self.h))  # rescaling the original image
        self.image = self.original_image  # the current image, which will be rotated
        self.rect = self.image.get_rect(center=(self.x, self.y))  # Initial rect at the center
