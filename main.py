# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:02:04 2023

@author: seyedmahmouds
"""

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
font_path = "./utils/Bangers-Regular.ttf"
font = pygame.font.Font(font_path, 64)

# Render the title text
title_text_surface = font.render("Akinator", True, color_font)

# Calculate the title text position
title_text_rect = title_text_surface.get_rect()
title_text_rect.center = (width // 2, height // 6)

# Define dimensions for the text box
box_width = title_text_rect.width + 40
box_height = title_text_rect.height + 40

# Calculate the position of the text box
box_x = (width - box_width) // 2
box_y = (height // 6) - (box_height // 2)


# Define dimensions for the buttons
button_width = 150
button_height = 60
button_spacing = 240


# Calculate the position of the "Yes" and "No" buttons
yes_button_x = (width - button_width - button_spacing) // 2
no_button_x = (width + button_spacing) // 2 - button_width
button_y = height - (button_height + 40)



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
    if title_text_rect.collidepoint(pygame.mouse.get_pos()):

        # Change the font color to the hover color
        text_surface = font.render("Akinator", True, color_hover)
    else:
        # Reset the font color to the default color
        text_surface = font.render("Akinator", True, color_font)

    # Draw the text box
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(screen, color_border, box_rect)
    pygame.draw.rect(screen, color_bg, box_rect.inflate(-10, -10))
    
    # Draw the "Yes" button
    yes_button_rect = pygame.Rect(yes_button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BLACK, yes_button_rect, 2)
    pygame.draw.rect(screen, WHITE, yes_button_rect.inflate(-10, -10))
    yes_text = font.render("Yes", True, BLACK)
    yes_text_rect = yes_text.get_rect(center=yes_button_rect.center)
    screen.blit(yes_text, yes_text_rect)
    
    # Draw the "No" button
    no_button_rect = pygame.Rect(no_button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BLACK, no_button_rect, 2)
    pygame.draw.rect(screen, WHITE, no_button_rect.inflate(-10, -10))
    no_text = font.render("No", True, BLACK)
    no_text_rect = no_text.get_rect(center=no_button_rect.center)
    screen.blit(no_text, no_text_rect)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if yes_button_rect.collidepoint(mouse_pos):
                if "yes" in current_node:
                    current_node = current_node["yes"]
                    if "answer" in current_node:
                        guessed = True
                        guess = current_node["answer"]
            elif no_button_rect.collidepoint(mouse_pos):
                if "no" in current_node:
                    current_node = current_node["no"]
                    if "answer" in current_node:
                        guessed = True
                        guess = current_node["answer"]

    # Draw the text on the screen
    screen.blit(text_surface, title_text_rect)

# Quit Pygame
pygame.quit()
