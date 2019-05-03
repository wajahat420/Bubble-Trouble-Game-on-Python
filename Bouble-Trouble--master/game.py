import pygame
import time

clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
lightBlue = (173,216,230)
color1= (101,45,104)
color2= (240,238,196)
color3= (247,148,30)
color4= (33,64,134)
color5= (0,230,118)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
img = pygame.image.load('player.png')
arrow = pygame.image.load('arrow.png')
lives = pygame.image.load('bonus life.png')
def things_dodged(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Ball Hits: "+str(count), True, black)
    gameDisplay.blit(text,(20,10))

class first:
    def __init__(self):
        self.ballx = 0
        self.bally = 0
        self.dirx = 4  
        self.diry = 6
        self.radius = 50
        self.rassi_x = 0
        self.rassi_y = 0
        self.level1 = 0
    def man(x,y):
        gameDisplay.blit(img,(x,y))
        clock.tick(90)

class ball_class:
    def ball_loop(self,ballx,bally,radius,dirx,diry):
        ball_big = first()
        ball_big.ballx = ballx
        ball_big.bally = bally
        ball_big.dirx = dirx
        ball_big.diry = diry
        ball_big.radius =  radius
        return ball_big
    def crash(self):
        font = pygame.font.SysFont("comicsansms", 80)
        text = font.render("YOU CRASHED", True, (255, 255, 255))
        gameDisplay.blit(text,(100,150))
        pygame.display.update()
        time.sleep(2)
    def WON(self):
        font = pygame.font.SysFont("comicsansms", 70)
        text = font.render("LEVEL COMPLETED", True, (255, 255, 255))
        gameDisplay.blit(text,(80,150))
        pygame.display.update()
        time.sleep(2)

    def over(self):
        font = pygame.font.SysFont("freesansbold.ttf", 60)
        text = font.render("GAME OVER", True, (0, 0, 0))
        gameDisplay.blit(text,(220,50))
        pygame.display.update()
        time.sleep(2)


    def rassi_func(self):
            self.rassi_x = -20
            self.rassi_y = 450
            self.rassi_diry = 0
            return self

    def end(self):
        font = pygame.font.SysFont("freesansbold.ttf", 80)
        text = font.render("Congratulations You Won", True, (0, 0, 0))
        gameDisplay.blit(text,(70,150))
        pygame.display.update()
        time.sleep(2)

        
    
    def start(self):
        font = pygame.font.SysFont("comicsansms", 80)
        text = font.render("Get Ready", True, (255, 255, 255))
        gameDisplay.blit(text,(180,150))
        pygame.display.update()
        time.sleep(2)
        
