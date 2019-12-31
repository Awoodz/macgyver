import pygame as pg
from macgyver_data import *
from macgyver_classes import *

item_sprite_img = pg.Surface(item_sprite_size)
item_sprite_img.fill(GREY)

"""lists, dictionnary and variable that will be used to build walls and determine position of elements"""
maze = [] # will contain the level file in array format
structure = [] # will convert maze array format into a list
position = {} # will contain every sprite positions (x, y format, in pixel)
actual_position = [] # determine player's position on the screen
key_position = 0 # will be used to determine keys in the position dictionnary

def main():

    picked_items = 0 # picked item counter

    Level.generate(maze) # Generate the maze
    Level.level_structure(maze, structure, position, key_position) # append lists and dictionnary that will be used

    macgyver = Player.rect_entity(structure, position, macgyver_start_point) # create macgyver rect
    guardian = Player.rect_entity(structure, position, guardian_start_point) # create guardian rect

    wall_structure = [index for index, value in enumerate(structure) if value==wall_tag] # create a list that will be used to display walls

    Player.__init__(macgyver ,actual_position, structure, position) # find the actual position of the player

    needle = Items.items_drop(structure, position, sprite_size) # create needle rect
    ether = Items.items_drop(structure, position, sprite_size) # create ether rect
    plastic = Items.items_drop(structure, position, sprite_size) # create plastic rect

    while not pg.Rect.colliderect(macgyver, guardian) : # as long as the player don't reach the guardian

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP: # if UP key is pressed, move up
                    Player.move_up(macgyver, actual_position, structure)
                if event.key == pg.K_DOWN: # if DOWN key is pressed, move down             
                    Player.move_down(macgyver, actual_position, structure)
                if event.key == pg.K_LEFT: # if LEFT key is pressed, move left               
                    Player.move_left(macgyver, actual_position, structure, position)          
                if event.key == pg.K_RIGHT: # if RIGHT key is pressed, move right
                    Player.move_right(macgyver, actual_position, structure, position)

        if pg.Rect.colliderect(macgyver, needle): # if the player touch the needle, it will be displayed in the collected items bar and not in the maze anymore
            needle = pg.Rect((0, sprite_height * sprite_nb_height), sprite_size)
            picked_items = picked_items + 1

        if pg.Rect.colliderect(macgyver, ether): # if the player touch the ether, it will be displayed in the collected items bar and not in the maze anymore
            ether = pg.Rect((sprite_width, sprite_height * sprite_nb_height), sprite_size)
            picked_items = picked_items + 1

        if pg.Rect.colliderect(macgyver, plastic): # if the player touch the plastic, it will be displayed in the collected items bar and not in the maze anymore
            plastic = pg.Rect((sprite_width * 2, sprite_height * sprite_nb_height), sprite_size)
            picked_items = picked_items + 1
    

        screen.fill(BLACK)
        screen.blit(item_sprite_img, (0, sprite_height * sprite_nb_height))
        screen.blit(macgyver_img, macgyver)
        Level.draw_wall(screen, wall_structure, position)
        screen.blit(guardian_img, guardian)
        screen.blit(needle_img, needle)
        screen.blit(ether_img, ether)
        screen.blit(plastic_img, plastic)
        pg.display.update()     

    if picked_items == 3:
        print("You win !")
    else:
        print("You lose !")

main()