import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill(pygame.Color(0,0,255))
test_rectangle = pygame.Rect(100,200,100,100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color(175,215,70))
    screen.blit(test_surface,(150,250))
    pygame.draw.rect(screen,pygame.Color('red'), test_rectangle)
    pygame.display.update()
    clock.tick(30)
    
