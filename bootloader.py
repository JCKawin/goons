import pygame
import settings as set

class loader():
    def __init__(self,main):
        self.screen = main.screen
        self.clock = main.clock
        self.text = pygame.font.Font(None,32)
        self.texter = self.text.render("Loading...",True,(255,255,255))
        self.progress = 0
        
    def run(self):
        while self.progress != 100: 
            rect = pygame.Rect(set.screen_res[0]/2 - 250 , set.screen_res[1]/2  ,400 * self.progress / 100 , 30)
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen , (255,255,255) , rect )
            self.screen.blit(self.texter , (set.screen_res[0]/2  - self.texter.get_width() , set.screen_res[1]/2 - self.texter.get_height()))
            self.progress += 1
            pygame.display.flip()
            self.clock.tick(60)
            
