import pygame
import time
import random
pygame.font.init()

WIDTH,HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space-War")
BG = pygame.transform.scale(pygame.image.load("1920x1080.jpg"),(WIDTH,HEIGHT))
PLY_WIDTH = 40
PLY_HEIGHT = 60
PLY_VEL = 5
FONT = pygame.font.SysFont("comicsans" , 50)
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

def draw(player, elapse_time,stars):
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN, "red", player)
    time_txt = FONT.render(f"Time: {round(elapse_time)}s", 1, "white")
    WIN.blit(time_txt,(10,10))
    for star in stars:
        pygame.draw.rect(WIN,"white",star)
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(500, HEIGHT - PLY_HEIGHT, PLY_WIDTH, PLY_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200,star_add_increment-50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x >=0:
            player.x -= PLY_VEL
        if keys[pygame.K_RIGHT] and player.x<=WIDTH-PLY_WIDTH:
            player.x += PLY_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + STAR_HEIGHT >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = FONT.render("YOU LOST!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time,stars)
    pygame.quit()



if __name__ == "__main__":
    main()