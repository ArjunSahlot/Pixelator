import pygame
import tkinter as tk

pygame.init()

WIDTH, HEIGHT = 1500, 950

FPS = 90

screen_width = tk.Tk().winfo_screenwidth()
screen_height = tk.Tk().winfo_screenheight()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

FONT = pygame.font.SysFont("comicsans", 45)
B_FONT = pygame.font.SysFont("comicsans", 55)
