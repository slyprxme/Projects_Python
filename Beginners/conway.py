# Rules:
# 1. A cell with fewer than two live neighbours dies (underpopulation)
# 2. A cell with two or more than two live neighbours stays alive (survival)
# 3. A cell with more than 3 live neighbours dies (overpopulation)
# 4. A dead cell with exactly 3 live neighbours becomes alive (reproduction)
# Step 1: Creating a grid
import random

import pygame

pygame.init()

bck = (0, 0, 0)
gry = (128, 128, 128)
ylw = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock

clock = pygame.time.Clock()


def gen(num):
    return set(
        [
            (random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH))
            for _ in range(num)
        ]
    )


def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)

        # *top_left unpacks the values from above
        pygame.draw.rect(screen, ylw, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, bck, (0, row * TILE_SIZE),
                         (WIDTH, row * TILE_SIZE))
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, bck, (col * TILE_SIZE, 0),
                         (col * TILE_SIZE, HEIGHT))


def adjust_grid(positions):
    all_neighbours = set()
    new_positions = set()

    for position in positions:
        neighbours = get_neighbour(position)
        all_neighbours.update(neighbours)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) in [2.3]:
            new_positions.add(position)

    for position in all_neighbours:
        neighbours = get_neighbour(position)

        neighbours = list(filter(lambda x: x in positions, neighbours))
        if len(neighbours) == 3:
            new_positions.add(position)


def get_neighbour(pos):
    pass


def main():
    running = True
    playing = False

    positions = set()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                col = x // TILE_SIZE
                row = y // TILE_SIZE

                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)

        screen.fill(gry)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
