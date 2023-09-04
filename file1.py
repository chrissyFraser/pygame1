import pygame


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('PyGame1')
clock = pygame.time.Clock()
test_font = pygame.font.Font('freesansbold.ttf', 32)


score_surface = test_font.render("score", False, "black").convert_alpha()
sky_surface = pygame.image.load("graphics/sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()

player_rect = player_surface.get_rect(midbottom = (50,300))
snail_rect = snail_surface.get_rect(midbottom = (600,300))
score_rect = score_surface.get_rect(center = (400,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("mouse collide")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))

    pygame.draw.rect(screen, "pink", score_rect)
    pygame.draw.rect(screen, "pink", score_rect, 5)
    # pygame.draw.line(screen, "blue", (0,0), (800,400))
    screen.blit(score_surface,score_rect)
    
    screen.blit(player_surface, player_rect)
    player_rect.left += 2
    if player_rect.left > 800:
        player_rect.right = 0
    
    screen.blit(snail_surface, snail_rect)
    snail_rect.left -= 1
    if snail_rect.right < 0:
        snail_rect.left = 800
    
    if player_rect.colliderect(snail_rect):
        print("collision")
    

    

    # mouse_position = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_position)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)

