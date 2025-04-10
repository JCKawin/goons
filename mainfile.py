import pygame
import m_char
import settings

class Goons():
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.setting = settings.setting(self)
        self.screen = pygame.display.set_mode(self.setting.screen_res,pygame.OPENGL)
        self.chrc = m_char.character(self)
        self.running: bool = True
        self.clock = pygame.time.Clock()

    def __del__(self):
         pygame.display.quit()
         pygame.quit()



    def rungame(self):
        while self.running:
             self._check_events()
             self._update_events()
      
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


    def _update_events(self):
         self.screen.fill((self.setting.bg_color))
         self.chrc.blitme()
    
         pygame.display.flip()
         self.clock.tick(60)
         










if __name__=="__main__":
    player: Goons = Goons()
    player.rungame()
    del player
