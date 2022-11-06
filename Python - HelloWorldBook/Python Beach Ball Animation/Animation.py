import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
ball_pos = [50,50]
ball_velocity = [10,7]
ball_size = 90

screen.blit(my_ball, ball_pos)
pygame.display.flip()

def wrapBall():
    if ball_pos[0] < 0-ball_size: ball_pos[0] = 640
    elif ball_pos[0] > 640: ball_pos[0] = 0-ball_size
    if ball_pos[1] < 0-ball_size: ball_pos[1] = 480
    elif ball_pos[1] > 480: ball_pos[1] = 0-ball_size

def bounceBall():
    if ball_pos[0] <= 0 or ball_pos[0] >= 640-ball_size: ball_velocity[0] *= -1
    if ball_pos[1] <= 0 or ball_pos[1] >= 480-ball_size: ball_velocity[1] *= -1

for i in range(0, 500):
    pygame.time.delay(20)
    screen.fill([255,255,255])
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]
    wrapBall()
    #bounceBall()
    screen.blit(my_ball, ball_pos)
    pygame.display.flip()
    


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
