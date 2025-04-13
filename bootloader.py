import pygame
import time
class loader():
    def __init__(self,main):
        self.screen = main.screen
        text = pygame.font.Font(None,32)
        texter = text.render("Loading...",True,(255,255,255))
        st = time.time()
        while int(time.time()  - st) != 5: 
            self.screen.fill((0,0,0))
            self.screen.blit(texter , (500,350))
            pygame.display.flip()
            main.clock.tick(60)
            
