import pygame

pygame.init()

class Bullet():

    def __init__(self,start_pos,end_pos,time_start,time_end,is_reversed):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.time_start = time_start
        self.time_end = time_end
        self.is_reversed = is_reversed

        if self.is_reversed:self.color = (255,0,0)
        else:self.color = (0,255,255)

    def update(self,screen,time):
        if self.time_start < time < self.time_end: 
            XXX = (time-self.time_start) / self.time_end
            pygame.draw.circle(screen,self.color,(int(self.start_pos[0]*XXX+self.end_pos[0]*(1-XXX)),int(self.start_pos[1]*XXX+self.end_pos[1]*(1-XXX))),2,0)




class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill((200,155,155))
        self.time = 0
        self.time_direction = 1
        self.clock = pygame.time.Clock()
        self.mainloop()

    
    def mainloop(self):
        while True:

            self.time += self.time_direction*self.clock.tick()/1000

            for bul in self.bullets:
                bul.update(self.screen,self.time)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.time_direction *= -1
                if event.type==pygame.QUIT:
                # if it is quit the game
                    pygame.quit()
                    exit(0)
            pygame.display.flip()


g = Game()