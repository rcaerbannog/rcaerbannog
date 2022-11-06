import pygame, sys, math, random

pygame.init()

#Settings
screen_width = 640
screen_height = 480
desired_fps = 60
ball_speed = 5
speed_increase = 0.1    #Speed increase per bounce
ai_maxspeed = 3
exponent = 1.3
controls_mode = "KEYBOARD" #Use "KEYBOARD" to use up and down arrow keys for control, or "MOUSE" to use mouse cursor
pygame.key.set_repeat(33, 1)

PI = math.pi
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, img_file, position, speed, direction):   #radians, from down (positive CCW)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

        self.speed = speed
        self.direction = direction
        self.position = position
        self.velocity = [speed*math.sin(self.direction),speed*math.cos(self.direction)]

    def move(self):
        if self.rect.left < 0 or self.rect.right > screen_width: self.direction = -self.direction
        if self.rect.top < 0 or self.rect.bottom > screen_height: self.direction = -(self.direction-PI/2)+PI/2
        if (self.direction < -PI): self.direction += 2*PI
        elif (self.direction > PI): self.direction -= 2*PI
        self.velocity = [self.speed*math.sin(self.direction),self.speed*math.cos(self.direction)]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.rect.left = int(round(self.position[0]))
        self.rect.top = int(round(self.position[1]))
        

class Paddle(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([10, 80])
        image_surface.fill([0,255,0])
        pygame.draw.rect(image_surface, [255,255,255], (0,0,10,80), 0)
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class AI():
    def __init__(self):
        self.prev_direction = 0
        self.target_y = None

    def ai(self, myBall, aiPaddle):   #Move towards ball impact (at screen_width - 40), += random choice of 30 pixels variance
        if myBall.direction != self.prev_direction:
            self.prev_direction = myBall.direction
            try:
                slope = (1/math.tan(myBall.direction))
            except ZeroDivisionError:
                slope = 0
            if myBall.direction > 0:
                self.target_y = int(round((myBall.rect.centery + slope*(screen_width-30-myBall.rect.left)))) + random.randint(-30,30)
            else:
                self.target_y = int(round((myBall.rect.centery - slope*(myBall.rect.left-30)))) + random.randint(-35,35)
                #Subtract because x direction is flipped: in QIII, cot(direction) is positive as well as ball.rect.left-30, but the ball is going up (lesser y)
            if self.target_y < aiPaddle.rect.height//2: self.target_y = aiPaddle.rect.height//2
            elif self.target_y > screen_height-aiPaddle.rect.height//2: self.target_y = screen_height-aiPaddle.rect.height//2
        #Movement
        if abs(aiPaddle.rect.centery-self.target_y) <= ai_maxspeed:
            aiPaddle.rect.centery = self.target_y
        elif aiPaddle.rect.centery < self.target_y:
            aiPaddle.rect.centery += ai_maxspeed  #Above target, so must increase y
        else:
            aiPaddle.rect.centery -= ai_maxspeed   #Below target, so must decrease y

def runGame():
    player_score = 0
    ai_score = 0
    ignore_collision = False

    score_font = pygame.font.Font(None, 50)
    player_score_surf = score_font.render(str(player_score), 1, (255,255,255))
    player_score_pos = [20,10]
    ai_score_surf = score_font.render(str(ai_score), 1, (255,255,255))
    ai_score_pos = [600,10]

    while player_score < 5 and ai_score < 5:
        myBall = Ball("wackyball.bmp", [320,240], ball_speed, PI/4)
        playerPaddle = Paddle([30,240])
        aiPaddle = Paddle([600,240])
        ballGroup = pygame.sprite.Group(myBall)
        gameAI = AI()
        screen.fill([0,0,0])

        running = True
        while running == True:
            clock.tick(desired_fps)
            screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "QUIT"
                elif controls_mode == "MOUSE" and event.type == pygame.MOUSEMOTION:
                    playerPaddle.rect.centery = event.pos[1]
                elif controls_mode == "KEYBOARD" and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and playerPaddle.rect.top > 0:
                        playerPaddle.rect.centery -= 5
                    elif event.key == pygame.K_DOWN and playerPaddle.rect.bottom < screen_height:
                        playerPaddle.rect.centery += 5
                        

            if ignore_collision:    #After bounce with paddle, wait one cycle to allow ball to move away to avoid glitching into paddle
                ignore_collision = False
                myBall.speed += speed_increase
            elif pygame.sprite.spritecollide(playerPaddle, ballGroup, False):
                dif = playerPaddle.rect.centery - myBall.rect.centery
                #Nonlinear direction output for ball bounce: direction related to impact distance from center of paddle
                #abs(dif/30) has value of [0,1] for difference of [0,30] so it should scale the same for any exponent
                myBall.direction = PI/2 + (PI/4)*abs(dif/30)**exponent if dif > 0 else PI/2 - (PI/4)*abs(dif/30)**exponent
                if myBall.direction < PI/4: myBall.direction = PI/4
                elif myBall.direction > 3*PI/4: myBall.direction = 3*PI/4
                ignore_collision = True
            elif pygame.sprite.spritecollide(aiPaddle, ballGroup, False):
                dif = aiPaddle.rect.centery - myBall.rect.centery
                myBall.direction = -PI/2 - (PI/4)*abs(dif/30)**exponent if dif > 0 else -PI/2 + (PI/4)*abs(dif/30)**exponent
                if myBall.direction > -PI/4: myBall.direction = -PI/4
                elif myBall.direction < -3*PI/4: myBall.direction = -3*PI/4
                ignore_collision = True
                
            myBall.move()
            gameAI.ai(myBall, aiPaddle)
            screen.blit(myBall.image, myBall.rect)
            screen.blit(playerPaddle.image, playerPaddle.rect)
            screen.blit(aiPaddle.image, aiPaddle.rect)

            if myBall.rect.left <= 0 or myBall.rect.right >= screen_width:
                running = False
                if (myBall.rect.left <= 0): ai_score += 1
                else: player_score += 1
                player_score_surf = score_font.render(str(player_score), 1, (255,255,255))
                ai_score_surf = score_font.render(str(ai_score), 1, (255,255,255))
                screen.blit(player_score_surf, player_score_pos)
                screen.blit(ai_score_surf, ai_score_pos)
                pygame.display.flip()
                pygame.time.delay(3000)
            else:
                screen.blit(player_score_surf, player_score_pos)
                screen.blit(ai_score_surf, ai_score_pos)
                pygame.display.flip()
                
            
    #End of while loop
    end_text = ""
    if (player_score == 5):
        end_text = "YOU WON"
    else:
        end_text = "YOU LOST"
    end_text_font = pygame.font.Font(None, 70)
    end_text_surf = end_text_font.render(end_text, 1, (255,255,255))
    screen.blit(end_text_surf, [screen.get_width()//2 - end_text_surf.get_width()//2,100])
    pygame.display.flip()
    pygame.time.delay(5000)
    return "GAME END"


#Main
exit_code = None
while (True):
    exit_code = runGame()
    if exit_code == "GAME END":
        print ("GAME END")
        break
    elif exit_code == "QUIT":
        print ("QUIT GAME")
        break
print("Pong by Alexander Li")
print("Exit code " + exit_code)
sys.exit(exit_code)
