import pygame 

pygame.init()

screen = pygame.display.set_mode ((800, 600))
clock = pygame.time.Clock ()
running = True  


class ScreenThing:
    def __init__(self, colors, speed):
        self.colors = list(colors)
    
        self.speed = int(speed * 10)
        

    def __str__(self):
        return(f"speed is {self.speed}. Colors is {self.colors}")
    
    def opration(self, colors, speed):

        for i in colors:
         screen.fill(i)
         pygame.display.flip()
         pygame.time.wait(speed)

while running:
    ScreenChange = ScreenThing(["purple", "blue", "pink", "black"], 10)
    ScreenChange.opration(ScreenChange.colors, ScreenChange.speed)


        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
