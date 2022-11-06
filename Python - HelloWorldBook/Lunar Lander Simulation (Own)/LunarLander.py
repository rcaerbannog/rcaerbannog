import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([400,600])
screen.fill([0,0,0])
ship = pygame.image.load("lunarlander.png")
moon = pygame.image.load("moonsurface.png")

#SETTINGS
ground = 540
start = 90

ship_mass = 5000.0
fuel = 5000.0
velocity = -100.0
gravity = 10
height = 2000
thrust = 0

delta_v = 0
y_pos = 90
held_down =False

class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([30,10])
        image_surface.fill([128,128,128])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location

def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    delta_t = 1/fps
    thrust = (500-myThrottle.rect.centery)*5.0
    fuel -= thrust/(10*fps)
    if fuel < 0: fuel = 0.0
    if fuel < 0.1: thrust = 0.0
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel))
    velocity += delta_v
    delta_h = velocity * delta_t
    height += delta_h
    y_pos = ground - (height * (ground - start) / 2000) - 90

def display_stats():
    v_str = f"velocity: {velocity:.0f} m/s"
    h_str = f"height: {height:.1f}"
    t_str = f"thrust: {thrust:.0f}"
    a_str = "acceleration: {delta_v * fps:.1f}"
    f_str = "fuel: {fuel:i}"
    
    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str, 1, (255,255,255))
    screen.blit(v_surf, [10,50])
    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255,255,255))
    screen.blit(a_surf, [10,100])
    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255,255,255))
    screen.blit(h_surf, [10,150])
    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, (255,255,255))
    screen.blit(t_surf, [10,200])
    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255,255,255))
    screen.blit(f_surf, [10,300])

def display_flames():
    flame_size = thrust/15
    for i in range(2):
        startx = 252 - 10 + 19*i
        starty = y_pos + 83
        pygame.draw.polygon(screen, [255,109,14], [(startx,starty),(startx+4,starty+flame_size),(startx+8,starty)], 0)

def display_final():
    final1 = "Game over"
    final2 = f"You landed at {velocity:.1f} m/s"
    final3 = None
    final4 = None
    if velocity > -5:
        final3 = "Nice landing!"
        final4 = "I hear NASA is hiring!"
    elif velocity > -15:
        final3 = "Ouch! A bit rough, but you survived."
        final4 = "You'll do better next time."
    else:
        final3 = "Yikes! You crashed a 30 billion dollar ship!"
        final4 = "Also, might be time to break out that cyanide capsule."

    pygame.draw.rect(screen, [0,0,0], [5,5,350,280], 0)
    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, (255,255,255))
    screen.blit(f1_surf, [20,50])
    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, (255,255,255))
    screen.blit(f2_surf, [20,110])
    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, (255,255,255))
    screen.blit(f3_surf, [20,150])
    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, (255,255,255))
    screen.blit(f4_surf, [20,180])
    pygame.display.flip()

myThrottle = ThrottleClass([15,500])
running = True
while running:
    clock.tick(30)
    fps = clock.get_fps()
    if fps<1: fps = 30
    if height > 0.01:
        calculate_velocity()
        screen.fill([0,0,0])
        display_stats()
        pygame.draw.rect(screen, [0,0,255], [80,350,24,100], 2)
        fuelbar = 96*fuel/500
        pygame.draw.rect(screen, [0,255,0], [84,448-fuelbar,18,fuelbar], 0)
        pygame.draw.rect(screen, [255,0,0], [25,300,10,200], 0)
        screen.blit(moon, [0,500,400,100])
        pygame.draw.rect(screen, [60,60,60], [220,535,70,5], 0)
        screen.blit(myThrottle.image, myThrottle.rect)
        display_flames()
        screen.blit(ship, [230,y_pos,50,90])
        instruct1 = "Land softly without running out of fuel"
        instruct2 = "Good landing: < 15m/s    Great landing: < 5m/s"
        inst1_font = pygame.font.Font(None, 24)
        inst2_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255,255,255))
        inst2_surf = inst2_font.render(instruct2, 1, (255,255,255))
        screen.blit(inst1_surf, [50,550])
        screen.blit(inst2_surf, [20,575])
        pygame.display.flip()
    else:
        display_final()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION and held_down:
            myThrottle.rect.centery = event.pos[1]
            if myThrottle.rect.centery < 300:
                myThrottle.rect.centery = 300
            elif myThrottle.rect.centery > 500:
                myThrottle.rect.centery = 500

pygame.quit()
                
        
    
    
