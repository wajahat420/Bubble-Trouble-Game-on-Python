import pygame

pygame.init()

display = pygame.display.set_mode((1100,600))
pygame.display.set_caption("Bubble Trouble")
Clock = pygame.time.Clock()
color = (255,50,50)
color1 = (50,255,150)
font = pygame.font.SysFont('georgia',65)
font1 = pygame.font.SysFont('georgia',55)

display.blit(font.render("Do you want to continue?", True,(color)),(180,120))

continue_button = pygame.draw.rect(display,((100,100,100)),(190,350,350,70))
quit_button = pygame.draw.rect(display,((100,100,100)),(690,350,190,70))
menu_button = pygame.draw.rect(display,((100,100,100)),(500,450,200,70))
display.blit(font1.render("CONTINUE?", True,(color1)),(200,350))
display.blit(font1.render("QUIT?", True,(color1)),(700,350))
display.blit(font1.render("MENU?", True,(color1)),(500,450))
pygame.display.flip()

pause = True
while pause:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                import firstLevel.py
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[1] >= 360:
                if pygame.mouse.get_pos()[0] <= 530 and pygame.mouse.get_pos()[1] <= 425:
                    import firstLevel.py
                        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 690 and pygame.mouse.get_pos()[1] >= 350:
                if pygame.mouse.get_pos()[0] <= 880 and pygame.mouse.get_pos()[1] <= 420:
                    pygame.quit()
                    quit()
                        #pause=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 450:
                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 520:
                    import menu

##        ok=pygame.mouse.get_pos()
##        print(ok)
Clock.tick(100)

pygame.quit()
