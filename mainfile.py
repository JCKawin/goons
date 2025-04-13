import pygame
import m_char
import settings
import bootloader

class Goons():
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode(settings.screen_res)
        self.chrc = m_char.character(self)
        self.running: bool = True
        self.clock = pygame.time.Clock()
        load = bootloader.loader(self)

    def __del__(self):
         pygame.display.quit()
         pygame.quit()



    def rungame(self):
        while self.running:
             self._update_events()
             self._check_events()
      
    def _check_events(self):
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT: self.running = False
                elif event.type == pygame.KEYDOWN: self._keydown(event)
                elif event.type == pygame.KEYUP: self._keyup(event)
                

    def _keydown(self,event):
         if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
              self.chrc.move_dir[3] = True
         if event.key == pygame.K_s or event.key == pygame.K_DOWN:
              self.chrc.move_dir[1] = True
         if event.key == pygame.K_a or event.key == pygame.K_LEFT:
              self.chrc.move_dir[2] = True
         if event.key == pygame.K_w or event.key == pygame.K_UP:
              self.chrc.move_dir[0] = True

    def _keyup(self,event):
         if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
              self.chrc.move_dir[3] = False
         if event.key == pygame.K_s or event.key == pygame.K_DOWN:
              self.chrc.move_dir[1] = False
         if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
              self.chrc.move_dir[2] = False
         if event.key == pygame.K_w or event.key == pygame.K_UP:
              self.chrc.move_dir[0] = False

         


    def _update_events(self):
         self.screen.fill((settings.bg_color))
         self.chrc.update()
         self.chrc.blitme()    
         pygame.display.flip()
         self.clock.tick(60)
         










if __name__=="__main__":
    player: Goons = Goons()
    player.rungame()
    del player
