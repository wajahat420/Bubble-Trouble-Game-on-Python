import pygame
pygame.init()
screen = pygame.display.set_mode((1100,500))
pygame.display.set_caption("Bubble trouble")
menu = True
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
orange = (255,75,74)
font1 = pygame.font.SysFont('georgia',35)
font = pygame.font.SysFont('georgia',70)
start_button = pygame.draw.rect(screen,(blue),(150,90,200,50))
credits_button = pygame.draw.rect(screen,(green),(210,160,200,50))
quit_button = pygame.draw.rect(screen,(red),(270,230,200,50))
highscore_button = pygame.draw.rect(screen,(purple),(210,300,200,50))
about_button = pygame.draw.rect(screen,(orange),(150,370,200,50))


screen.blit(font.render('Bubble Trouble!!', True, (white)), (515, 195))
screen.blit(font1.render('Play!', True, (white)), (215, 95))
screen.blit(font1.render('Credits..', True, (white)), (245, 165))
screen.blit(font1.render('Quit?', True, (white)), (325, 235))
screen.blit(font1.render('High Scores', True, (white)), (215, 305))
screen.blit(font1.render('About', True, (white)), (205, 375))
#pygame.display.update()
pygame.display.flip()


def Game():
    screen.fill((0,0,0))
    #Clock.tick(60)
    pygame.display.flip()
    import firstLevel
def Credits():
    screen.fill((0,0,0))
    pygame.display.flip()
    import creditss
def Highscores():
    screen.fill((0,0,0))
    pygame.display.flip()
    import HighScores
def Quit():
    pygame.quit()
    quit() 
def About():
    screen.fill((0,0,0))
    pygame.display.flip()
    import about
def Pause():
    screen.fill((0,0,0))
    pygame.display.flip()
    import pause

while menu:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 230:
                if pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] <= 280:
                        Quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                if pygame.mouse.get_pos()[0] <= 450 and pygame.mouse.get_pos()[1] <= 140:
                        Game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 210 and pygame.mouse.get_pos()[1] >= 160:
                if pygame.mouse.get_pos()[0] <= 410 and pygame.mouse.get_pos()[1] <= 210:
                        Credits()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 210 and pygame.mouse.get_pos()[1] >= 300:
                if pygame.mouse.get_pos()[0] <= 410 and pygame.mouse.get_pos()[1] <=350 :
                        Highscores()   
        if event.type == pygame.MOUSEBUTTONDOWN:
           if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 370:
                if pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] <=420:
                        About()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                Pause()

    
