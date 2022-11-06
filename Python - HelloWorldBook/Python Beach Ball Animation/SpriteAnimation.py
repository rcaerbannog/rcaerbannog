import pygame, sys, random

class MyBallClass (pygame.sprite.Sprite):
    def __init__(self, image_file, position, velocity = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.velocity = [0,0] if velocity == None else velocity

    def moveBounce(self):
        self.rect = self.rect.move(self.velocity)
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

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])

img_file = "beach_ball.png"
balls = []
for row in range(0, 3):
    for column in range(0, 3):
        position = [column*180 + 10, row*180 + 10]
        velocity = [random.randint(-5, 5), random.randint(-5, 5)]
        ball = MyBallClass(img_file, position, velocity)
        balls.append(ball)

for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    screen.fill([255,255,255])
    for ball in balls:
        ball.moveBounce()
        #ball.moveWrap()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
pygame.quit()
