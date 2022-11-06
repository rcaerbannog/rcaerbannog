import pygame, sys, random

class MyBallClass (pygame.sprite.Sprite):
    def __init__(self, image_file, start_position, velocity = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = start_position
        self.velocity = [0,0] if velocity == None else velocity

    def moveBounce(self):
        self.rect = self.rect.move(self.velocity)
        print(self.rect)
        if self.rect.left < 0 or self.rect.right > width:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.velocity[1] *= -1

    def moveWrap(self):
        self.rect = self.rect.move(self.velocity)
        if self.rect.right < 0: self.rect.left = width
        elif self.rect.left > width: self.rect.right = 0
        if self.rect.bottom < 0: self.rect.top = height
        elif self.rect.top > height: self.rect.bottom = 0

pygame.init()

pygame.key.set_repeat(1, 30)

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

img_file = "beach_ball.png"
my_ball = MyBallClass(img_file, [50,50], [3,2])
screen.blit(my_ball.image, my_ball.rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: my_ball.rect.top -= 5
            elif event.key == pygame.K_DOWN: my_ball.rect.top += 5
#        elif event.type == pygame.MOUSEMOTION:
#            my_ball.rect.center = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN: held = True
        elif event.type == pygame.MOUSEBUTTONUP: held = False
        elif event.type == pygame.USEREVENT:
            print ("TIMER")
    clock.tick(30)
    my_ball.moveBounce()
    screen.fill([255,255,255])
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
pygame.quit()
