import pygame
import settings as set

class object(pygame.sprite.Sprite):
    def __init__(self, main):
        super().__init__()
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()
        self.Ohandle = pygame.image.load("images\\object.bmp")
        self.handle_rect = self.Ohandle.get_rect()
        self.handle_rect = (set.screen_res[0]*8/9,set.screen_res[1]/2)
        self.handle = pygame.transform.scale(self.Ohandle , (128,128))

    def blitme(self):
        self.screen.blit(self.handle,self.handle_rect)