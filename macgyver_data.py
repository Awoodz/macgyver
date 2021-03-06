"""SPRITE"""
# sprite height (pixel)
SPRT_HGT = 43
# number of sprite in screen height
SPRT_NB_HGT = 10
# sprite width (pixel)
SPRT_WDTH = 43
# number of sprite in screen width
SPRT_NB_WDTH = 15
# sprite size (pixel)
SPRT_SZ = (SPRT_WDTH, SPRT_HGT)

"""PICKED ITEMS BOX 1"""
# picked item surface height
ITM_SPRT_HGT = 70

"""COLOR"""
BLACK = (0, 0, 0)

"""SCREEN"""
# screen width
SCRN_WDTH = SPRT_NB_WDTH * SPRT_WDTH
# screen height
SCRN_HGT = (SPRT_NB_HGT * SPRT_HGT) + ITM_SPRT_HGT
# screen size
SCRN_SZ = (SCRN_WDTH, SCRN_HGT)

"""PICKED ITEMS BOX 2"""
# picked item pygame surface
ITM_HUB_POS = (0, SPRT_NB_HGT * SPRT_HGT)
# position of needle in item hub
NEEDLE_HUB_POS = (97, 444)
# position of ether in item hub
ETHER_HUB_POS = (290, 444)
# position of plastic tub in item hub
PLASTIC_HUB_POS = (498, 444)

"""PICTURES"""
# macgyver sprite path
MACGYVER_IMG_PATH = "ressource/MacGyver.png"
# guardian sprite path
GUARDIAN_IMG_PATH = "ressource/Gardien.png"
# wall sprite path
WALL_IMG_PATH = "ressource/wall_tile.png"
# floor sprite path
FLOOR_IMG_PATH = "ressource/floor_tile.png"
# plastic tube sprite path
PLASTIC_IMG_PATH = "ressource/tube_plastique_resize.png"
# needle sprite path
NEEDLE_IMG_PATH = "ressource/aiguille_resize.png"
# ether sprite path
ETHER_IMG_PATH = "ressource/ether_resize.png"
# item hub sprite path
ITM_HUB_IMG_PATH = "ressource/item_hub.png"
# win screen image path
WIN_IMG_PATH = "ressource/you_win.png"
# lose screen image path
LOSE_IMG_PATH = "ressource/you_lose.png"

"""CHARACTERS IN MAZE"""
# Macgyver start point character
MG_STARTP = "M"
# Guardian start point character
GUARDIAN_STARTP = "G"
# wall character
WALL_TAG = 1
# item character
ITEM_TAG = "X"
# void character
VOID_TAG = 0

"""MAZE LIST"""
LEVEL_CHOICE = [
    "ressource/level1.txt",
    "ressource/level2.txt"
]

"""ITEM"""
# number of item to pick in order to win
ITM_TO_PICK = 3

"""SOUND"""
# picking item sound path
PICKED_SOUND_PATH = "ressource/pickup.wav"
# win sound path
WIN_SOUND_PATH = "ressource/you_win.wav"
# lose sound path
LOSE_SOUND_PATH = "ressource/you_lose.wav"
# music sound path
LEVEL_MUSIC_PATH = "ressource/music8b.wav"
