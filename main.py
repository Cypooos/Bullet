import pygame
import math
import random
pygame.init()

class Bullet():

    def __init__(self,start_pos,end_pos,time_start,time_end,is_reversed=False):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.time_start = time_start
        self.time_end = time_end
        self.is_reversed = is_reversed

        if self.is_reversed:self.color = (0,255,255)
        else:self.color = (255,0,0)

    def update(self,screen,time,player,dir_):
        if self.time_start < time < self.time_end: 
            XXX = (time-self.time_start) / (self.time_end-self.time_start)
            pygame.draw.circle(screen,self.color,(int(self.start_pos[0]*XXX+self.end_pos[0]*(1-XXX)),int(self.start_pos[1]*XXX+self.end_pos[1]*(1-XXX))),4,0)
            if (dir_ == 1) != self.is_reversed: return False
            if -3 <= self.start_pos[0]*XXX+self.end_pos[0]*(1-XXX)-player.pos[0] <= 3 and -3 <= self.start_pos[1]*XXX+self.end_pos[1]*(1-XXX)-player.pos[1] <= 3:
                print("TOUCHE")
                return True
        return False

class Player():

    speed = 200
    speed2 = 50

    def __init__(self,pos):
        self.pos = pos
        self.vies = 3
    
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(int(self.pos[0]),int(self.pos[1])),2,0)
            


class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.time = 0
        self.time_direction = 1
        self.clock = pygame.time.Clock()
        self.player = Player([200,200])

        self.bullets = []
        def generate_side(side,start,rev,number=50,off=None,end=None):
            if off == None:off=random.randint(0,int(number/400))
            if end == None: end=start+5
            if side == "left":
                for i in range(number):self.bullets.append(Bullet([0,400-i*(400/number)-off],[400,400-i*(400/number)-off],start,end,rev))
            if side == "right":
                for i in range(number):self.bullets.append(Bullet([400,400-i*(400/number)-off],[0,400-i*(400/number)-off],start,end,rev))
            if side == "up":
                for i in range(number):self.bullets.append(Bullet([i*(400/number)-off,400],[i*(400/number)-off,0],start,end,rev))
            if side == "down":
                for i in range(number):self.bullets.append(Bullet([i*(400/number)-off,0],[i*(400/number)-off,400],start,end,rev))
        
        def generate_circle(from_,start,rev,number=50,off=None,end=None):
            if off == None:off=random.randint(0,10_000)/(400/number)
            if end == None: end=start+5
            if from_ == "out":
                for i in range(number):
                    i = (i+off)/(number/2)
                    self.bullets.append(Bullet([math.cos(i*math.pi)*400+200,math.sin(i*math.pi)*400+75],[200,75],start,end,rev))
            if from_ == "center":
                for i in range(number):
                    i = (i+off)/(number/2)
                    self.bullets.append(Bullet([200,75],[math.cos(i*math.pi)*400+200,math.sin(i*math.pi)*400+75],start,end,rev))

        def generate_spiral(from_,start,rev,off,branches,duration=1,dense=10):
            if from_ == "out":
                for x in range(duration*dense):
                    generate_circle("out",x/dense+start,rev,branches,(x/dense)*off)
            if from_ == "center":
                for x in range(duration*dense):
                    generate_circle("center",x/dense+start,rev,branches,(x/dense)*off)
        
        def horrible():
            generate_side("up",1,True,100,end=5)
            generate_side("down",0,False,100,end=4)
            generate_side("up",3,True,100,end=7)
            generate_side("down",2,False,100,end=6)
            generate_side("up",5,True,100,end=9)
            generate_side("down",4,False,100,end=8)
            generate_side("up",7,True,100,end=11)
            generate_side("down",6,False,100,end=10)
            generate_circle("center",3,False)
            generate_circle("out",3,True)
            generate_circle("center",2,False)
            generate_circle("out",2,True)
            generate_circle("center",4,False)
            generate_circle("out",4,True)
            generate_circle("center",5,False)
            generate_circle("out",5,True)
            generate_circle("center",6,False)
            generate_circle("out",6,True)
            generate_circle("center",8,False)
            generate_circle("out",8,True)
            generate_circle("center",9,False)
            generate_circle("out",9,True)
            return
        
        def long_():
            for x in range(2000):generate_circle("out",x/200,True,1)
            for x in range(2000):generate_circle("center",x/200,False,1)
        
        def spiral():
            generate_spiral("out",0,True,3.2,5,10,20)
            generate_spiral("center",0,False,3.2,5,10,20)
            generate_spiral("out",2,True,0.2,9,3)
            generate_spiral("center",2,False,0.2,9,3)
            generate_spiral("out",5,True,-0.2,9,3)
            generate_spiral("center",5,False,-0.2,9,3)

        horrible()
        
        """
        generate_side("up",1,True,20)
        generate_side("down",1,True,20)
        
        """
        """
        generate_side("left",1,False,20)
        generate_side("right",1,False,20)
        
        """



        self.mainloop()

    
    def mainloop(self):
        while True:
            delta = self.clock.tick()/1000

            self.time += self.time_direction*delta

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.time_direction *= -1
                if event.type==pygame.QUIT:
                # if it is quit the game
                    pygame.quit()
                    exit(0)

            
            keys=pygame.key.get_pressed()
            if keys[pygame.K_w]:sp = self.player.speed2
            else: sp = self.player.speed
            if keys[pygame.K_LEFT]:self.player.pos[0] -= delta*sp
            if keys[pygame.K_RIGHT]:self.player.pos[0] += delta*sp
            if keys[pygame.K_UP]:self.player.pos[1] -= delta*sp
            if keys[pygame.K_DOWN]:self.player.pos[1] += delta*sp
            if self.player.pos[0] > 400:self.player.pos[0] = 400
            if self.player.pos[1] > 400:self.player.pos[1] = 400
            if self.player.pos[0] < 0:self.player.pos[0] = 0
            if self.player.pos[1] < 0:self.player.pos[1] = 0

            if self.time_direction == 1: self.screen.fill((100,55,55))
            if self.time_direction == -1: self.screen.fill((55,100,100))

            for bul in self.bullets:
                if bul.update(self.screen,self.time,self.player,self.time_direction):
                    self.player.pos = [200,200]
            self.player.draw(self.screen)
            pygame.display.flip()


g = Game()