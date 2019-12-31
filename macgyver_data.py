import pygame as pg
import sys, os

# SPRITE
sprite_height = 43
sprite_nb_height = 10 # number of sprite in height
sprite_width = 43
sprite_nb_width = 15 # number of sprite in width
sprite_size = (sprite_width, sprite_height)

# ITEM SPRITE --- show which items get picked up
item_sprite_height = 50

# SCREEN
screen_width = sprite_nb_width * sprite_width
screen_height = (sprite_nb_height * sprite_height) + item_sprite_height
screen_size = (screen_width, screen_height)
screen = pg.display.set_mode(screen_size)

# ITEM SPRITE --- show which items get picked up
item_sprite_size = (screen_width, item_sprite_height)

# COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)

# IMAGES
macgyver_img = pg.image.load("ressource/MacGyver.png")
guardian_img = pg.image.load("ressource/Gardien.png")
wall_img = pg.image.load("ressource/wall_tile.png")
plastic_img = pg.image.load("ressource/tube_plastique_resize.png")
needle_img = pg.image.load("ressource/aiguille_resize.png")
ether_img = pg.image.load("ressource/ether_resize.png")

macgyver_start_point = "M"
guardian_start_point = "G"
wall_tag = 1

level_choice = ["level1.txt", "level2.txt"]

