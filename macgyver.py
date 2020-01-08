import pygame as pg
from macgyver_data import *
from player_class import *
from level_class import *
from items_class import *
from helpers import end

"""lists, dictionnary and variable that will be used"""
"""to build walls and determine position of elements"""
maze = []  # will contain the level file in array format
struct = []  # will convert maze array format into a list
pos = {}  # will contain every sprite positions (x, y format, in pixel)
actual_pos = []  # determine player's position on the screen
# screen pygame surface
scrn = pg.display.set_mode(SCRN_SZ)
# images load
macgyver_img = pg.image.load(MACGYVER_IMG_PATH)
guardian_img = pg.image.load(GUARDIAN_IMG_PATH)
wall_img = pg.image.load(WALL_IMG_PATH)
floor_img = pg.image.load(FLOOR_IMG_PATH)
plastic_img = pg.image.load(PLASTIC_IMG_PATH)
needle_img = pg.image.load(NEEDLE_IMG_PATH)
ether_img = pg.image.load(ETHER_IMG_PATH)
itm_hub_img = pg.image.load(ITM_HUB_IMG_PATH)
win_img = pg.image.load(WIN_IMG_PATH)
lose_img = pg.image.load(LOSE_IMG_PATH)
# initiate the pygame sound mixe
pg.mixer.init()
# sound played when an item is picked up
picked_sound = pg.mixer.Sound(PICKED_SOUND_PATH)
# sound played when the player win
win_sound = pg.mixer.Sound(WIN_SOUND_PATH)
# sound played when the player lose
lose_sound = pg.mixer.Sound(LOSE_SOUND_PATH)
# music played in background
level_music = pg.mixer.music.load(LEVEL_MUSIC_PATH)


def main():
    """Launch the Macgyver game !"""
    # picked item counter
    picked_items = 0
    # Generate the maze
    Level.generate(maze)
    # append lists and dictionnary that will be used
    Level.level_structure(maze, struct, pos)
    # create macgyver rect
    macgyver = Player.rect_entity(struct, pos, MG_STARTP)
    # create guardian rect
    guardian = Player.rect_entity(struct, pos, GUARDIAN_STARTP)
    # create a list that will be used to display walls
    wall_structure = [
        index for index, value in enumerate(struct) if value == WALL_TAG
    ]
    # create a list that will be used to display floor
    floor_structure = [
        index for index, value in enumerate(struct) if value != WALL_TAG
    ]
    # find the actual position of the player
    Player.__init__(macgyver, actual_pos, struct, pos)
    # create needle rect
    needle = Items.items_drop(struct, pos, SPRT_SZ)
    # create ether rect
    ether = Items.items_drop(struct, pos, SPRT_SZ)
    # create plastic rect
    plastic = Items.items_drop(struct, pos, SPRT_SZ)
    # play the background music
    pg.mixer.music.play()

    # as long as the player don't reach the guardian
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                # if UP key is pressed, move up
                if event.key == pg.K_UP:
                    Player.move_up(macgyver, actual_pos, struct)
                # if DOWN key is pressed, move down
                if event.key == pg.K_DOWN:
                    Player.move_down(macgyver, actual_pos, struct)
                # if LEFT key is pressed, move left
                if event.key == pg.K_LEFT:
                    Player.move_left(macgyver, actual_pos, struct, pos)
                # if RIGHT key is pressed, move right
                if event.key == pg.K_RIGHT:
                    Player.move_right(macgyver, actual_pos, struct, pos)

        # if the player touch the needle, it will be displayed
        # in the collected items bar and not in the maze anymore
        if pg.Rect.colliderect(macgyver, needle):
            needle = pg.Rect(NEEDLE_HUB_POS, SPRT_SZ)
            picked_sound.play()
            picked_items = picked_items + 1

        # if the player touch the ether, it will be displayed
        # in the collected items bar and not in the maze anymore
        if pg.Rect.colliderect(macgyver, ether):
            ether = pg.Rect(ETHER_HUB_POS, SPRT_SZ)
            picked_sound.play()
            picked_items = picked_items + 1

        # if the player touch the plastic, it will be displayed
        # it will be displayed in the collected items bar and not
        # in the maze anymore
        if pg.Rect.colliderect(macgyver, plastic):
            plastic = pg.Rect(PLASTIC_HUB_POS, SPRT_SZ)
            picked_sound.play()
            picked_items = picked_items + 1

        pg.display.update()
        scrn.fill(BLACK)
        # display the walls
        Level.draw_level(scrn, wall_structure, pos, wall_img)
        # display the floor tiles
        Level.draw_level(scrn, floor_structure, pos, floor_img)
        # display Macgyver
        scrn.blit(macgyver_img, macgyver)
        # display the guardian
        scrn.blit(guardian_img, guardian)
        # display the picked items surface
        scrn.blit(itm_hub_img, ITM_HUB_POS)
        # display the needle
        scrn.blit(needle_img, needle)
        # display the ether
        scrn.blit(ether_img, ether)
        # display the plastic tub
        scrn.blit(plastic_img, plastic)

        # check if players picked up all items
        if pg.Rect.colliderect(macgyver, guardian):
            if picked_items == ITM_TO_PICK:
                end(scrn, win_img, win_sound)
            else:
                end(scrn, lose_img, lose_sound)


main()
