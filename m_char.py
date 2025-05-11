import pygame
import settings

class character(pygame.sprite.Sprite):
    def __init__(self,main):
        super().__init__()
        self.screen = main.screen
        self.screen_rect = main.screen.get_rect()

        self.image = pygame.image.load("images\\goon_mc.png")
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
        # [ up0 , down1 , right2 , left3 ]
        self.move_dir = [False , False , False , False]

    def update(self):
        if self.rect.right != self.screen_rect.right and self.move_dir[3]:
            self.rect.x += settings.m_speed
        if self.rect.left != self.screen_rect.left and self.move_dir[2]:
            self.rect.x -= settings.m_speed
        if self.rect.top != self.screen_rect.top and self.move_dir[0]:
            self.rect.y -= settings.m_speed
        if self.rect.bottom != self.screen_rect.bottom and self.move_dir[1]:
            self.rect.y += settings.m_speed

        
   
    def blitme(self):
        self.screen.blit(self.image , self.rect)

    



        

