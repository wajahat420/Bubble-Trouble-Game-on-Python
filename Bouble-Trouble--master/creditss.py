import pygame

pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Credits")
Clock = pygame.time.Clock()
color = (150,0,10)
color1 = (150,150,130)
green=(0,255,0)
white=(255,255,255)
font = pygame.font.SysFont('georgia',45)
font1 = pygame.font.SysFont('georgia',55)
font2 = pygame.font.SysFont('georgia',35)


display.blit(font.render("Welcome to Bubble Trouble.", True,(color)),(40,30))
display.blit(font.render("This game is made with lots of effort. Enjoy!", True,(color)),(40,90))
display.blit(font1.render("Credits:", True,(color1)),(30,170))

display.blit(font.render(">Wajahat Sarwat", True,(color1)),(100,260))
display.blit(font.render(">Muhamaad Hamza", True,(color1)),(140,330))
display.blit(font.render(">Muhammad Anas", True,(color1)),(180,400))
display.blit(font.render(">Muhammad Saad", True,(color1)),(220,470))
pygame.display.flip()

credits = True
while credits:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #credits = False   		
    #mouse=pygame.mouse.get_pos()
    #print(mouse)
Clock.tick(100)
