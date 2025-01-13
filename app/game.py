import pygame
from app import config, display
from customObjects import custom_text, custom_images, custom_button

# Copyight (C) 2025  Hohenzoler
# #
# # This program is free software; you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation; version 2 of the License.
# #
# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# # GNU General Public License for more details.
# #
# # You should have received a copy of the GNU General Public License along
# # with this program; if not, write to the Free Software Foundation, Inc.,
# # 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.r
class Game:
    def __init__(self):
        pygame.init()

        config.set_config()

        self.cfg = config.read_config()

        self.version = self.cfg['version']
        self.width = int(self.cfg['width'])
        self.height = int(self.cfg['height'])
        self.fps = float(self.cfg['fps'])
        self.title = self.cfg['title']
        self.fullscreen = int(self.cfg['full-screen'])
        self.enable_debug = int(self.cfg['enable_debug'])

        print(f'PYGAME-STARTING-PROJECT, Copyright (C) 2024 Hohenzoler\nPYGAME-STARTING-PROJECT comes with ABSOLUTELY NO WARRANTY\nThis is free software, and you are welcome to redistribute it under certain conditions; Go to License.md for more info.')

        self.objects_in_memory = 0
        self.clock = pygame.time.Clock()
        self.font = None


        self.run = True


        self.objects = []

        self.screen = pygame.display.set_mode((self.width, self.height))
        if self.fullscreen:
            pygame.display.toggle_fullscreen()
        pygame.display.set_caption(f"{self.title} (v {self.version})")


        self.displays = {'template_display': display.basic_display(self), 'game_display': display.game_display(self)}
        self.current_display = self.displays['game_display']

        self.pointing_at = []


        self.debug = False
        self.debug_items = [custom_text.Custom_text(self, 12, 15, f'Current version: {self.version}', text_color='white', font=self.font, font_height=30,  center=False),
                            custom_text.Custom_text(self, 12, 45, f'Resolution: {self.width}x{self.height}', font=self.font, font_height=30, text_color='white', center=False),
                            custom_text.Custom_text(self, 12, 75, f'FPS cap: {self.fps}', font=self.font, font_height=30,  text_color='white', center=False),
                            custom_text.Custom_text(self, 12, 105, f'FPS: {self.clock.get_fps()}', font=self.font, font_height=30,  text_color='white', center=False),
                            custom_text.Custom_text(self, 12, 135, f'Objects in memory: {self.current_display.objects_in_memory}', font=self.font, font_height=30,  text_color='white', center=False),
                            custom_text.Custom_text(self, 12, 165, f'Current display: {type(self.current_display)}', font=self.font, font_height=30,  text_color='white', center=False)]

        for debug_item in self.debug_items:
            debug_item.hidden = True

    def mainloop(self):
        while self.run:
            self.current_display.mainloop()
            self.events()
            self.render()
            self.update()
            self.clock.tick(self.fps)




    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSLASH and self.enable_debug:
                self.debug = not self.debug
                for di in self.debug_items:
                    di.hidden = not di.hidden
            else:
                self.current_display.events(event)

    def render(self):
        self.screen.fill('black')
        self.current_display.render()

        for object in self.objects:
            object.render()



    def update(self):
        if self.debug:

            self.debug_items[3].update_text(f'FPS: {self.clock.get_fps()}')
            self.debug_items[4].update_text(f'Objects in memory: {self.current_display.objects_in_memory}')
            self.debug_items[5].update_text(f'Current display: {type(self.current_display)}')


        pygame.display.update()
        pygame.display.flip()

