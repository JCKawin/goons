import pygame
import sys
import settings as set

class gameover():
    def __init__(self,main):
        pygame.init()
        self.screen = main.screen
        self.text = pygame.font.Font(None,144)
        self.texter = "GAME OVER!!!"
        self.text_image = self.text.render( '*', True, (0,0,0) )
        self.text_cursor = 0
        self.next_update = 0

    def run(self):
        while True:
            clock = pygame.time.get_ticks()     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    
            self.screen.fill( (0,0,0 ) )
            self.screen.blit( self.text_image, (set.screen_res[0]/2 -380,set.screen_res[1]/2-self.text_image.get_height()/2))

   
            if ( clock > self.next_update ):

                self.next_update = clock + 150
                if ( self.text_cursor < len( self.texter ) ):
       
                    self.text_cursor += 1
        
                self.text_image = self.text.render( self.texter[0:self.text_cursor], True, (255,255,255) )

            pygame.display.flip()
