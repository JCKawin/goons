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
            self.screen.fill((255,255,255))
            self.clock.tick(60)
            pygame.display.flip()










player: Goons = Goons()
player.run_game()
