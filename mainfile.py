import pygame
import sys
import m_char

class Goons():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,400))
        self.running: bool = True
        self.clock = pygame.time.Clock()
        self.chrc = m_char.character(self)


    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.chrc.blitme()
            pygame.display.update()
            self.screen.fill((0,0,0))
            self.clock.tick(60)
            pygame.display.flip()









if __name__=="__main__":
    player: Goons = Goons()
    player.run_game()
