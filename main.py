import pygame, random


# variables
COLOR_SNAKE = (55,220,10)
COLOR_FONDO = (0,0,0)
COLOR_FOOD = (169,6,6)
COLOR_SCORE = (200,60,80)
GRIS = (50,50,50)

NX = 50
NY = 50
DIM = 15
ANCHURA = NX*DIM
ALTURA = NY*DIM


# inicio del juego
pygame.init()

play_surface = pygame.display.set_mode((ANCHURA, ALTURA))
pygame.display.set_caption("Snake. Creado por: Javier Abollado")

font = pygame.font.Font(None, 30)
FPS = pygame.time.Clock()


# funciones
def food():
    x_pos = random.randint(0,NX-1)*DIM
    y_pos = random.randint(0,NY-1)*DIM
    food_pos = [x_pos, y_pos]
    return food_pos

def actualizar_screen(snake_body, food_pos, score, fps):
    play_surface.fill(COLOR_FONDO)

    for i in range(NY+1):
        pygame.draw.rect(play_surface, GRIS, pygame.Rect(0, i*DIM-1, ANCHURA, 2))
    for i in range(NY+1):
        pygame.draw.rect(play_surface, GRIS, pygame.Rect(i*DIM-1, 0, 2, ALTURA))

    for pos in snake_body:
        pygame.draw.rect(play_surface, COLOR_SNAKE, pygame.Rect(pos[0], pos[1], DIM, DIM))

    pygame.draw.rect(play_surface, COLOR_FOOD, pygame.Rect(food_pos[0], food_pos[1], DIM, DIM))
        
    text = font.render(str(score),0, COLOR_SCORE)
    play_surface.blit(text, (ANCHURA-40,20))

    FPS.tick(fps)


def main():

    snake_pos = [10*DIM, 5*DIM]
    snake_body = [[10*DIM, 5*DIM]]
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP6:
                    change = "RIGHT"
                if event.key == pygame.K_KP4:
                    change = "LEFT"
                if event.key == pygame.K_KP8:
                    change = "UP"
                if event.key == pygame.K_KP5:
                    change = "DOWN"

        # movimiento de la serpiente
        if change == "RIGHT":
            snake_pos[0] += DIM
        if change == "LEFT":
            snake_pos[0] -= DIM
        if change == "UP":
            snake_pos[1] -= DIM
        if change == "DOWN":
            snake_pos[1] += DIM

        if snake_pos in snake_body: 
            run = False 

        # actualizar movimientos
        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            food_pos = food()
            score += 1
        else:
            snake_body.pop()

        # colorear todos los objetos de la pantalla
        actualizar_screen(snake_body, food_pos, score, 10)


        # condiciones para finalizar
        if snake_pos[0] <= 0 or snake_pos[0] >= ANCHURA or snake_pos[1] <= 0 or snake_pos[1] >= ALTURA:
            run = False

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()