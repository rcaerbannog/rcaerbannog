import pygame, sys, math

#SETTINGS
screen_width = 640
screen_height = 480
ai_maxSpeed = 20
desired_fps = 30

pygame.init()
PI = math.pi
clock = pygame.time.Clock()
screen = pygame.display.set_mode([screen_width, screen_height])

class Ball(pygame.sprite.Sprite):
    def __init__(self, img_file, position, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.velocity = velocity

    def move(self):
        if self.rect.left < 0 or self.rect.right > screen_width: self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height: self.velocity[1] *= -1
        self.rect = self.rect.move(self.velocity)
        

class Paddle(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([10, 80])
        image_surface.fill([255,255,255])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.center = location


#Preparation
myBall = Ball("wackyball.bmp", [320,240], [8,5])
playerPaddle = Paddle([30,240])
aiPaddle = Paddle([610,240])
ballGroup = pygame.sprite.Group(myBall)
screen.fill([0,0,0])


#Main
running = True
while running:
    clock.tick(desired_fps)
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            playerPaddle.rect.centery = event.pos[1]

    if pygame.sprite.spritecollide(playerPaddle, ballGroup, False):
        myBall.velocity[0] *= -1
        myBall.velocity[1] = int(round(5*(myBall.rect.centery - playerPaddle.rect.centery)/(playerPaddle.rect.height/2)))
    elif pygame.sprite.spritecollide(aiPaddle, ballGroup, False):
        myBall.velocity[0] *= -1
        myBall.velocity[1] = int(round(5*(myBall.rect.centery - aiPaddle.rect.centery)/(aiPaddle.rect.height/2)))
        
    myBall.move()
    #AI CODE
    #PLACEHOLDER
    aiPaddle.rect.centery = myBall.rect.centery

    #Allow ball velocity to take non-integer values and keep track of ball position independent of screen
    
    
    screen.blit(myBall.image, myBall.rect)
    screen.blit(playerPaddle.image, playerPaddle.rect)
    screen.blit(aiPaddle.image, aiPaddle.rect)
    pygame.display.flip()

print("GAME ENDED")
sys.exit(0)
