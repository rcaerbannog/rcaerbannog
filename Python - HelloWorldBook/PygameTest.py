import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])

for i in range (0, 100):
    rand_rect = pygame.Rect(random.randint(0, 250), random.randint(0, 100),
                     random.randint(0, 400), random.randint(0, 500))
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pygame.draw.rect(screen, color, rand_rect, 2)
    pygame.time.delay(50)
    pygame.display.flip()
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
