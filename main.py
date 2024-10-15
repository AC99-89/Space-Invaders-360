#basic pygame running
import pygame
import sys

#pygame setup
class Game():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Space Invaders 360")
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.Surface((int(self.width), int(self.height)))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            #poll for events
            #pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            #Fill the screen with a color to wipe away anything from the last frame
            self.screen.fill("purple")

            #Render your game here

            #flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60) #limits FPS to 60

        # pygame.quit()
        # sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()