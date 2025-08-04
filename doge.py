import os
import time
import random
import sys

WIDTH = 20
HEIGHT = 10
PLAYER = '🟩'
BLOCK = '🟥'
EMPTY = '⬛'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(player_pos, blocks):
    grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for b in blocks:
        if 0 <= b[1] < HEIGHT:
            grid[b[1]][b[0]] = BLOCK
    grid[HEIGHT - 1][player_pos] = PLAYER
    return grid

def draw_grid(grid):
    for row in grid:
        print(''.join(row))

def get_input(timeout=0.5):
    import select
    print("Move [A/D]: ", end='', flush=True)
    i, _, _ = select.select([sys.stdin], [], [], timeout)
    if i:
        key = sys.stdin.readline().strip().lower()
        return key
    return None

def update_blocks(blocks):
    new_blocks = []
    for b in blocks:
        new_blocks.append((b[0], b[1] + 1))
    return new_blocks

def check_collision(blocks, player_pos):
    for b in blocks:
        if b[1] == HEIGHT - 1 and b[0] == player_pos:
            return True
    return False

def play():
    player_pos = WIDTH // 2
    blocks = []
    score = 0

    while True:
        clear()
        blocks = update_blocks(blocks)

        if random.random() < 0.3:
            blocks.append((random.randint(0, WIDTH - 1), 0))

        if check_collision(blocks, player_pos):
            break

        grid = create_grid(player_pos, blocks)
        draw_grid(grid)
        print(f"\nScore: {score}")

        key = get_input(0.2)
        if key == 'a' and player_pos > 0:
            player_pos -= 1
        elif key == 'd' and player_pos < WIDTH - 1:
            player_pos += 1

        blocks = [b for b in blocks if b[1] < HEIGHT]
        score += 1

    clear()
    print("💥 YOU DIED 💥")
    print(f"Final Score: {score}")

def main():
    try:
        while True:
            play()
            again = input("\nPlay again? (y/n): ").lower()
            if again != 'y':
                print("Later nerd 👋")
                break
    except KeyboardInterrupt:
        print("\nBye bye 😪")

if __name__ == "__main__":
    main()
