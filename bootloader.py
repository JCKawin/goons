import pygame
import time
import settings as set

class loader():
    def __init__(self,main):
        self.screen = main.screen
        text = pygame.font.Font(None,32)
        texter = text.render("Loading...",True,(255,255,255))
        progress = 0
        while progress != 100: 
            rect = pygame.Rect(set.screen_res[0]/2 - 250 , set.screen_res[1]/2  ,400 * progress / 100 , 30)
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen , (255,255,255) , rect )
            self.screen.blit(texter , (set.screen_res[0]/2  - texter.get_width() , set.screen_res[1]/2 - texter.get_height()))
            progress += 1
            pygame.display.flip()
            main.clock.tick(60)
            
