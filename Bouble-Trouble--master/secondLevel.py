import json
from game import *
#from firstlevel import *
class second_Level(object):
    def second_level(xyz,aa,bb,cc,dd,ee,ff):
        v = 0
        while True:
            pygame.init()
         
            x = display_width * 0.34 
            y = display_height * 0.94
            
            score = 35
            time = 20
            ball_big = first()
            ball_big.ballx = 100
            ball_big.bally = 150
            radius = 30
            ball_big.dirx = 3
            ball_big.diry = 5
            x_change = 0
            crash = False
            var = ball_class()
            rassi = var.rassi_func()
            ball_list = []
            rassi_list = []
            
            ball_big = var.ball_loop(ball_big.ballx,ball_big.bally,radius
                                     ,ball_big.dirx,ball_big.diry)
            ball_list.append(ball_big)
            ball_big = var.ball_loop(400,ball_big.bally,radius
                                     ,ball_big.dirx,ball_big.diry)
            ball_list.append(ball_big)       
            
            rassi_list.append(rassi)
            
            
            while not crash:
                
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        elif event.key == pygame.K_RIGHT:
                            x_change = 5
                        elif event.key == pygame.K_SPACE:
                            rassi.rassi_x = x
                            rassi.rassi_y = 450
                            rassi.rassi_diry = 6
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x_change = 0
                for rassi in rassi_list:
                    rassi.rassi_y -= rassi.rassi_diry
                    if rassi.rassi_y <0:
                        var.rassi_func()
                for ball_big in ball_list:
                    ball_big.ballx += ball_big.dirx
                    ball_big.bally += ball_big.diry
                        
                    if ball_big.ballx > display_width - ball_big.radius or ball_big.ballx < 30:
                        ball_big.dirx *= -1
                    if ball_big.bally > display_height - ball_big.radius or ball_big.bally < 150:
                        ball_big.diry *= -1
                    if ball_big.radius != 0:
                        if  not( ball_big.ballx + ball_big.radius < x or ball_big.ballx - ball_big.radius > x + 30 \
                            or ball_big.bally + ball_big.radius < y):
                            crash = True
                            xyz += 1
                            if xyz == 1:
                                aa = -20
                                bb = -20
                                var.crash()
                            if xyz == 2:
                                cc = -30
                                dd = -30
                                var.crash()
                            if xyz == 3:
                                ee = -40
                                ff = -40

                    else:
                        ball_list.remove(ball_big)
                
                    if not(ball_big.ballx + ball_big.radius < rassi.rassi_x or  ball_big.ballx - ball_big.radius > rassi.rassi_x \
                       or rassi.rassi_y > ball_big.bally + ball_big.radius):
                        ball_big.radius += -10
                        ball_big.diry = 4
                        ball_big = var.ball_loop(ball_big.ballx,ball_big.bally,ball_big.radius,ball_big.dirx,ball_big.diry)
                        ball_list.append(ball_big)
                        ball_big.dirx *= -1
                        var.rassi_func()
                        score += 5
                    
                        record = {'highscore':score}
                        
                        with open("my_file.txt", "w") as f_out:
                            json.dump(record, f_out)
                        with open("my_file.txt") as f:
                            saved_record = json.load(f)
                        
                    if len(ball_list) == 0:
                        var.end()
                        import menu
                pygame.draw.rect(gameDisplay,color3,[0,0,display_width,display_height])
                pygame.draw.rect(gameDisplay,color4,[30,40,display_width-60,display_height-70])


                
                for ball_big in ball_list:
                    pygame.draw.circle(gameDisplay, color5, [ball_big.ballx, ball_big.bally], ball_big.radius)
                for live in range(3):
                    gameDisplay.blit(lives,(aa,bb))
                    gameDisplay.blit(lives,(cc,dd))
                    gameDisplay.blit(lives,(ee,ff))

                    
                for rassi in rassi_list:
                    gameDisplay.blit(arrow,(rassi.rassi_x,rassi.rassi_y))
                if xyz == 3:
                    var.over()
                    pygame.quit()
                    quit()
                if x<0:
                    x=0
                if x>780:
                    x=780
                things_dodged(score)    
                x += x_change
                b = first
                b.man(x,y)
                if v == 0:
                    var.start()
                v=1
                pygame.display.flip()
x= second_Level()
