import pygame
import sys

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,1000))
        self.clock = pygame.time.Clock()
        self.image1 = pygame.image.load("Picture-export.png")
        self.image1.set_colorkey((37, 150, 190))
        self.impos = [100, 100]
        self.movement = [False, False]

        self.colarea = pygame.Rect(50, 50, 300, 50)
    def run(self):
        
        while True:
            im_r = pygame.Rect(self.impos[0], self.impos[1], self.image1.get_width(), self.image1.get_height())
            self.screen.fill("gray")  
            self.impos[1] += (self.movement[1] - self.movement[0]) * 10
            self.screen.blit(self.image1, (self.impos))
            if im_r.colliderect(self.colarea):
                pygame.draw.rect(self.screen, (100, 100, 100), self.colarea)
                self.movement[0] = False
                self.movement[1] = False
            else:
                pygame.draw.rect(self.screen, (110, 100, 100), self.colarea )
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False


                        


            pygame.display.update()
            self.clock.tick(60)

Main().run()

