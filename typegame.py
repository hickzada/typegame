import pygame
import random
import time

# Inicialização do pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurando a tela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Digitação")

# Definindo a fonte
font = pygame.font.Font(None, 74)

# Lista de palavras
words = ["programming", "python", "keyboard", "developer", "code", "computer", "game"]

# Função principal do jogo
def game():
    score = 0
    word = random.choice(words)
    x = random.randint(0, WIDTH - 100)
    y = random.randint(0, HEIGHT - 100)
    input_box = pygame.Rect(200, 500, 140, 32)
    user_text = ''
    clock = pygame.time.Clock()
    start_time = time.time()

    run = True
    while run:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text == word:
                        score += 1
                        word = random.choice(words)
                        x = random.randint(0, WIDTH - 100)
                        y = random.randint(0, HEIGHT - 100)
                        user_text = ''
                        start_time = time.time()
                    else:
                        user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        # Checando o tempo
        if time.time() - start_time > 5:
            word = random.choice(words)
            x = random.randint(0, WIDTH - 100)
            y = random.randint(0, HEIGHT - 100)
            start_time = time.time()

        # Desenhando a palavra e a entrada do usuário
        text = font.render(word, True, BLACK)
        screen.blit(text, (x, y))
        txt_surface = font.render(user_text, True, BLACK)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, RED, input_box, 2)

        # Atualizando a tela
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    game()
