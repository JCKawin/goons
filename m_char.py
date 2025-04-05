import pygame

class character(pygame.sprite.Sprite):
    def __init__(self,main):
        super().__init__()
        self.screen = main.screen
        self.screen_rect = main.screen.get_rect()

        self.image = pygame.image.load("images\\m_char.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = 256
        self.rect.y = 256
   
    def blitme(self):
        self.screen.blit(self.image , self.rect)

    



        

