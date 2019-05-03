import pygame

pygame.init()

display = pygame.display.set_mode((870,550))
pygame.display.set_caption("About")
Clock = pygame.time.Clock()
color = (150,0,10)
green= (0,255,0)
white=(255,255,255)
color1 = (150,150,130)
font = pygame.font.SysFont('georgia',65)
font1 = pygame.font.SysFont('georgia',35)
display.blit(font.render("ABOUT", True,(color)),(300,40))
#display.blit(font.render("This game is made with lots of effort. Enjoy!", True,(color)),(40,90))
#display.blit(font1.render("Credits:", True,(color1)),(30,170))

display.blit(font1.render(" So want to know how to play bubble trouble?", True,(color1)),(30,170))

display.blit(font1.render("Well it is pretty simple.There is a player and ", True,(color1)),(30,220))
display.blit(font1.render("the player can move left or right and it has the ability", True,(color1)),(30,270))
display.blit(font1.render("to shoot string towards the ball. The ball will bounce", True,(color1)),(30,320))
display.blit(font1.render("all over the window and the player has to avoid", True,(color1)),(30,370))
display.blit(font1.render("getting in contact with the ball.", True,(color1)),(30,420))
display.blit(font1.render("If the ball hits the player, then the game is over.", True,(color1)),(30,470))
pygame.display.flip()


credits = True
while credits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            credits = False
    #mouse=pygame.mouse.get_pos()
    #print(mouse)
Clock.tick(100)
pygame.quit()
