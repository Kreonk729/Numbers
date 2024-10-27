import pygame
import random
import sys


FPS = 60
NUM_COUNT = 12000
NUMBERS = []  
MAX_DISTANCE = 200  
WIDTH = 800
HEIGHT = 600  


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Numbers")
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры камеры
camera_x, camera_y, camera_z = 0, 0, 0
camera_speed = 5


def generate_number(camera_x, camera_y):
    x = random.randint(camera_x - 2000, camera_x + 2000)
    y = random.randint(camera_y - 2000, camera_y + 2000)
    z = random.randint(1, MAX_DISTANCE) 
    return (x, y, z)


for _ in range(NUM_COUNT):
    NUMBERS.append(generate_number(camera_x, camera_y))


def draw_numbers():
    visible_count = 0  
    for x, y, z in NUMBERS:
        # Применяем смещение камеры
        screen_x = int(WIDTH / 2 + (x - camera_x) * (300 / z))
        screen_y = int(HEIGHT / 2 + (y - camera_y) * (300 / z))

        if 0 <= screen_x < WIDTH and 0 <= screen_y < HEIGHT:
            size = max(10, int(300 / z))  
            font = pygame.font.SysFont("Arial", size)
            text = font.render(str(z), True, WHITE)
        
            screen.blit(text, (screen_x, screen_y))
            visible_count += 1  


    font = pygame.font.SysFont("Rubik", 30)
    counter_text = font.render(f"Visible Numbers: {visible_count}", True, WHITE)
    screen.blit(counter_text, (10, 10)) 


def update_numbers():
    global NUMBERS


    while len(NUMBERS) < NUM_COUNT:
        NUMBERS.append(generate_number(camera_x, camera_y))


    NUMBERS = [num for num in NUMBERS if num[2] > camera_z - 500]  

# Главный игровой цикл
def main():
    global camera_x, camera_y, camera_z, screen, WIDTH, HEIGHT
    fullscreen = False  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            camera_x -= camera_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            camera_x += camera_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            camera_y -= camera_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            camera_y += camera_speed
        if keys[pygame.K_q]:
            camera_z -= camera_speed
        if keys[pygame.K_e]:  
            camera_z += camera_speed


        update_numbers()  
        screen.fill(BLACK)  
        draw_numbers()  
        pygame.display.flip()  
        clock.tick(FPS)  

if __name__ == "__main__":
    main()
