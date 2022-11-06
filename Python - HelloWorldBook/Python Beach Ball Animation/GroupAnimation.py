import pygame, sys, random, math

desired_fps = 60
clock = pygame.time.Clock()
fps_ratio = 1
frames = 0
seconds = 0

class MyBallClass (pygame.sprite.Sprite):
    def __init__(self, image_file, position, velocity = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.velocity = [0,0] if velocity == None else velocity

    def moveBounce(self):
        #self.rect = self.rect.move(self.velocity)
        self.rect = self.rect.move([int(round(self.velocity[0]*fps_ratio)), int(round(self.velocity[1]*fps_ratio))])
        if self.rect.left < 0 or self.rect.right > width:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.velocity[1] *= -1

    def moveWrap(self):
        #self.rect = self.rect.move(self.velocity)
        self.rect = self.rect.move([int(round(velocity[0]*fps_ratio)), int(round(velocity[1]*fps_ratio))])
        if self.rect.right < 0: self.rect.left = width
        elif self.rect.left > width: self.rect.right = 0
        if self.rect.bottom < 0: self.rect.top = height
        elif self.rect.top > height: self.rect.bottom = 0

def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        ball.moveBounce()
        #ball.moveWrap()
        screen.blit(ball.image, ball.rect)
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball, group, False):
            ball.velocity[0] *= -1
            ball.velocity[1] *= -1
        group.add(ball)
    pygame.display.flip()

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])


img_file = "beach_ball.png"
group = pygame.sprite.Group()
for row in range(0, 3):
    for column in range(0, 3):
        position = [column*180 + 10, row*180 + 10]
        velocity = [random.randint(-5, 5), random.randint(-5, 5)]
        ball = MyBallClass(img_file, position, velocity)
        group.add(ball)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(desired_fps)
    actual_fps = clock.get_fps()
    fps_ratio = 1 if actual_fps <= 0 else desired_fps / actual_fps
    frames += 1
    if (frames % desired_fps == 0):
        frames = 0
        seconds += 1
        print (str(actual_fps) + "    " + str(round(fps_ratio, 5)))
    screen.fill([255,255,255])
    animate(group)
    pygame.display.flip()
pygame.quit()
