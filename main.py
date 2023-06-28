import pygame
from pygame.locals import *
import pygame.font

# Initialize Pygame
pygame.init()

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

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Purple-Blue Ombre")

# Define gradient colors
color_bottom = (148, 0, 211)   # Purple
color_top = (0, 0, 255)  # Blue

# Define colors for the text box
color_bg = (255, 255, 255)  # White
color_border = (0, 0, 0)    # Black
color_font = (255, 223, 0)  # Gold
color_hover = (255, 0, 0)   # Red (hover color)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load custom font
font = pygame.font.Font(None, 64)

# Render the text
text_surface = font.render("Akinator", True, color_font)

# Calculate the text position
text_rect = text_surface.get_rect()
text_rect.center = (width // 2, height // 6)

# Define dimensions for the text box
box_width = text_rect.width + 40
box_height = text_rect.height + 40

# Calculate the position of the text box
box_x = (width - box_width) // 2
box_y = (height // 6) - (box_height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
   
    if guessed:
        text = font.render("I guess it's " + guess + "!", True, BLACK)
    else:
        text = font.render(current_node["question"], True, BLACK)

    text_rect2 = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect2)

    pygame.display.update()

    # Fill the screen with an ombre gradient
    for y in range(width):

        # Calculate the interpolation factor based on the y-position
        interp = y / height

        # Interpolate the RGB values between color_top and color_bottom
        r = int((1 - interp) * color_top[0] + interp * color_bottom[0])
        g = int((1 - interp) * color_top[1] + interp * color_bottom[1])
        b = int((1 - interp) * color_top[2] + interp * color_bottom[2])
        color = (r, g, b)

        # Draw a row with the calculated color
        pygame.draw.rect(screen, color, pygame.Rect(0, y, width, 1))

    # Check if the mouse is over the text
    if text_rect.collidepoint(pygame.mouse.get_pos()):

        # Change the font color to the hover color
        text_surface = font.render("Akinator", True, color_hover)
    else:
        # Reset the font color to the default color
        text_surface = font.render("Akinator", True, color_font)

    # Draw the text box
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, color_border, box_rect)
    pygame.draw.rect(screen, color_bg, box_rect.inflate(-10, -10))

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

# Quit Pygame
pygame.quit()
