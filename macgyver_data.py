import pygame as pg

"""SPRITE"""
# sprite height (pixel)
sprt_hgt = 43
# number of sprite in screen height
sprt_nb_hgt = 10
# sprite width (pixel)
sprt_wdth = 43
# number of sprite in screen width
sprt_nb_wdth = 15
# sprite size (pixel)
sprt_sz = (sprt_wdth, sprt_hgt)

"""PICKED ITEMS BOX 1"""
# picked item surface height
itm_sprte_hgt = 50

"""SCREEN"""
# screen width
scrn_wdth = sprt_nb_wdth * sprt_wdth
# screen height
scrn_hgt = (sprt_nb_hgt * sprt_hgt) + itm_sprte_hgt
# screen size
scrn_sz = (scrn_wdth, scrn_hgt)
# screen pygame surface
scrn = pg.display.set_mode(scrn_sz)

"""PICKED ITEMS BOX 2"""
# picked item pygame surface
itm_sprt_sz = (scrn_wdth, itm_sprte_hgt)

"""COLORS"""
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

"""PICTURES"""
macgyver_img = pg.image.load("ressource/MacGyver.png")
guardian_img = pg.image.load("ressource/Gardien.png")
wall_img = pg.image.load("ressource/wall_tile.png")
plastic_img = pg.image.load("ressource/tube_plastique_resize.png")
needle_img = pg.image.load("ressource/aiguille_resize.png")
ether_img = pg.image.load("ressource/ether_resize.png")

"""CHARACTERS IN MAZE"""
# Macgyver start point character
mg_startp = "M"
# Guardian start point character
guardian_start_point = "G"
# wall character
wall_tag = 1

"""MAZE LIST"""
level_choice = ["level1.txt", "level2.txt"]

"""ITEM"""
# number of item to pick in order to win
itm_to_pick = 3
