import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BUTTON_COLOR = WHITE
BUTTON_HOVER_COLOR = (200, 200, 200)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# The list of possible words
words = ["hangman", "python", "pygame", "random", "words", "guess"]

# The word to guess
word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters = []
mistakes = 0
game_over = False

# The "Play Again" button
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 100, 50)

def draw():
    # Clear the screen
    win.fill(WHITE)

    # Draw the word
    text = font.render(" ".join(guessed), True, (0, 0, 0))
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Draw the guessed letters
    guessed_text = font.render("Guessed letters: " + ", ".join(guessed_letters), True, (0, 0, 0))
    win.blit(guessed_text, (10, HEIGHT - 40))

    # Draw the mistake counter
    mistakes_text = font.render("Mistakes: " + str(mistakes), True, (0, 0, 0))
    win.blit(mistakes_text, (10, 10))

    # Check if the game is over
    if "_" not in guessed:
        win_text = font.render("You Win!", True, (0, 0, 0))
        win.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2 + 50))
        pygame.draw.rect(win, BUTTON_COLOR, button_rect)
        button_text = font.render("Play Again", True, (0, 0, 0))
        win.blit(button_text, (button_rect.x + button_rect.width // 2 - button_text.get_width() // 2, button_rect.y + button_rect.height // 2 - button_text.get_height() // 2))
    elif mistakes > 7:
        lose_text = font.render("You Lose!", True, (0, 0, 0))
        win.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2 - lose_text.get_height() // 2 + 50))

    # Flip the display
    pygame.display.flip()

def reset_game():
    global word, guessed, guessed_letters, mistakes, game_over
    word = random.choice(words)
    guessed = ["_"] * len(word)
    guessed_letters = []
    mistakes = 0
    game_over = False

def main():
    global mistakes, game_over
    clock = pygame.time.Clock()

    while True:
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and button_rect.collidepoint(pygame.mouse.get_pos()):
                    reset_game()
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.unicode.isalpha():  # only accept alpha keys
                    letter = event.unicode
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter in word:
                            for i, l in enumerate(word):
                                if l == letter:
                                    guessed[i] = letter
                        else:
                            mistakes += 1
                            if mistakes > 7:
                                game_over = True

        clock.tick(60)

if __name__ == "__main__":
    main()
