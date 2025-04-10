import pygame
import sys
import m_char
import settings

class Goons():
    def __init__(self):
        pygame.init()
        self.setting = settings.setting(self)
        self.screen = pygame.display.set_mode(self.setting.screen_res)
        self.chrc = m_char.character(self)
        self.running: bool = True
        self.clock = pygame.time.Clock()



    def rungame(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((self.setting.bg_color))
            self.chrc.blitme()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(30)









if __name__=="__main__":
    player: Goons = Goons()
    player.rungame()
