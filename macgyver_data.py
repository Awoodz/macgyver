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
itm_sprte_hgt = 70

"""COLOR"""
BLACK = (0, 0, 0)

"""SCREEN"""
# screen width
scrn_wdth = sprt_nb_wdth * sprt_wdth
# screen height
scrn_hgt = (sprt_nb_hgt * sprt_hgt) + itm_sprte_hgt
# screen size
scrn_sz = (scrn_wdth, scrn_hgt)

"""PICKED ITEMS BOX 2"""
# picked item pygame surface
itm_hub = (0, 430)
needle_hub_pos = (97, 444)
ether_hub_pos = (290, 444)
plastic_hub_pos = (498, 444)

"""PICTURES"""
macgyver_img_path = "ressource/MacGyver.png"
guardian_img_path = "ressource/Gardien.png"
wall_img_path = "ressource/wall_tile.png"
plastic_img_path = "ressource/tube_plastique_resize.png"
needle_img_path = "ressource/aiguille_resize.png"
ether_img_path = "ressource/ether_resize.png"
itm_hub_img_path = "ressource/item_hub.png"
win_img_path = "ressource/you_win.png"
lose_img_path = "ressource/you_lose.png"

"""CHARACTERS IN MAZE"""
# Macgyver start point character
mg_startp = "M"
# Guardian start point character
guardian_start_point = "G"
# wall character
wall_tag = 1
# item character
item_tag = "X"
# void character
void_tag = 0

"""MAZE LIST"""
level_choice = ["level1.txt", "level2.txt"]

"""ITEM"""
# number of item to pick in order to win
itm_to_pick = 3
picked_sound_path = "ressource/pickup.wav"
win_sound_path = "ressource/you_win.wav"
lose_sound_path = "ressource/you_lose.wav"
