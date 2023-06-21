import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Akinator")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define fonts
font = pygame.font.SysFont(None, 32)

# Define the decision tree
decision_tree = {
    "question": "Is the character fictional?",
    "yes": {
        "question": "Is the character from a video game?",
        "yes": {
            "question": "Is the character a hero?",
            "yes": {
                "answer": "Mario"
            },
            "no": {
                "answer": "Bowser"
            }
        },
        "no": {
            "question": "Is the character from a movie?",
            "yes": {
                "answer": "Darth Vader"
            },
            "no": {
                "answer": "Sonic the Hedgehog"
            }
        }
    },
    "no": {
        "answer": "Albert Einstein"
    }
}

# Game state variables
current_node = decision_tree
guessed = False
guess = ""

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                if "yes" in current_node:
                    current_node = current_node["yes"]
                    if "answer" in current_node:
                        guessed = True
                        guess = current_node["answer"]
            elif event.key == pygame.K_n:
                if "no" in current_node:
                    current_node = current_node["no"]
                    if "answer" in current_node:
                        guessed = True
                        guess = current_node["answer"]

    # Clear the screen
    window.fill(WHITE)

    # Display the current question
    question_text = font.render(current_node["question"], True, BLACK)
    window.blit(question_text, (100, 100))

    # Display the guess if reached
    if guessed:
        guess_text = font.render("Is your character " + guess + "?", True, BLACK)
        window.blit(guess_text, (100, 200))

    # Update the display
    pygame.display.update()
