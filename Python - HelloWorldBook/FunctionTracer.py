import pygame, sys, math

origin = [320, 240]

# Amplitude 150, period 100
def sinFunc(x):
    return 150*math.sin(math.pi*x/50)

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

f = sinFunc
plot_points = []
for x in range (-320, 321):
    y = int(f(x))
    plot_points.append([origin[0] + x, origin[1] + y])
pygame.draw.lines(screen, [0,0,0], False, plot_points, 2)
pygame.display.flip()

running = True
while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
pygame.quit()
    
