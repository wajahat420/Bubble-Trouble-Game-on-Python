import pygame

pygame.init()

display = pygame.display.set_mode((700,550))
pygame.display.set_caption("Credits")
Clock = pygame.time.Clock()
color = (150,0,10)
color1 = (150,150,130)
green=(0,255,0)
white=(255,255,255)
font = pygame.font.SysFont('georgia',65)
font1 = pygame.font.SysFont('georgia',35)

display.blit(font.render("HIGH SCORES", True,(color)),(140,40))

instructText = font1.render("my_file.txt", True, white)
with open("my_file.txt") as f:
    instructText = font1.render(f.read(), True, white)
with open("my_file.txt") as f:
    for line in f:
        instructText = font1.render(line, True, white)
        
text_rect = instructText.get_rect()

display.blit(instructText, (220,250),text_rect)

pygame.display.flip()

    
credits = True
while credits:
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #crashed=False
            #credits = False
    #mouse=pygame.mouse.get_pos()
    #print(mouse)
Clock.tick(100)

pygame.quit()
