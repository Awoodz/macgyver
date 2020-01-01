import pygame as pg
import random
from macgyver_data import *


class Level:

    def generate(self):
        """Convert the txt file into an array named "maze" """
        with open(random.choice(level_choice)) as level_file:
            for line in level_file:
                level_lines = []
                for sprite in line:
                    if sprite == '0':
                        # the code need numbers to be int format
                        sprite = int(sprite)
                    if sprite == '1':
                        # the code need numbers to be int format
                        sprite = int(sprite)
                    if sprite != '\n':
                        level_lines.append(sprite)
                self.append(level_lines)

    def level_structure(maze, structure, position, key_position):
        """ From the generated array, will create a list of every sprite
        in the array and a dictionnary of every position on screen """
        for j, line in enumerate(maze):
            for i, case in enumerate(line):
                structure.append(case)
                # Keys in position dictionnary will be the same
                # that the indexes of the structure list.
                position[key_position] = (i*sprt_wdth, j*sprt_hgt)
                key_position = key_position + 1

    def draw_wall(surface, wall_structure, position):
        """ Display walls on the screen """
        for elements in wall_structure:
            scrn.blit(wall_img, position[elements])


class Player:

    def __init__(self, actual_position, struct, position):
        """find the starting position + define the start
        position as actual position (only at initialization)"""
        # Search for the index in structure list that is equal
        #  to the macgyver start point caracter and create a list
        #  with all those index
        start_position = [
            index for index, values in enumerate(struct) if values == mg_startp
            ]
        # avoid a bug when start point is upper left corner...
        if start_position == []:
            # ...giving it a value = 0
            start_position.append(0)
        actual_position.append(start_position)

    def rect_entity(struct, position, ent_start):
        """create rect for entities such as macgyver or the guardian"""
        # Search for the index in structure list that is equal
        # to the entity start point caracter and create a list
        # with all those index
        entity = [
            index for index, values in enumerate(struct) if values == ent_start
            ]
        for elements in entity:
            return pg.Rect(position[elements], sprt_sz)

    def move_up(self, actual_position, structure):
        """ Move the character up if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the top border of the screen
            if (elements - sprt_nb_wdth) >= 0:
                # if the upper sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements - sprt_nb_wdth] == 1:
                    # ...move up !
                    self.move_ip(0, - sprt_hgt)
                    # define the new actual position
                    actual_position[0] = [elements - sprt_nb_wdth]

    def move_down(self, actual_position, structure):
        """ Move the character down if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the bottom border of the screen
            if (elements + sprt_nb_wdth) <= (sprt_nb_wdth * sprt_nb_hgt - 1):
                # if the bottom sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements + sprt_nb_wdth] == 1:
                    # ...move down !
                    self.move_ip(0, sprt_hgt)
                    # define the new actual position
                    actual_position[0] = [elements + sprt_nb_wdth]

    def move_left(self, actual_position, structure, position):
        """ Move the character left if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the left border of the screen
            if not position[elements] <= (sprt_wdth, (0-scrn_hgt)):
                # if the left sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements - 1] == 1:
                    # ...move left !
                    self.move_ip(- sprt_wdth, 0)
                    # define the new actual position
                    actual_position[0] = [elements - 1]

    def move_right(self, actual_position, structure, position):
        """ Move the character right if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the right border of the screen
            if not position[elements] >= (scrn_wdth - sprt_wdth, (0-scrn_hgt)):
                # if the right sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements + 1] == 1:
                    # ...move right !
                    self.move_ip(sprt_wdth, 0)
                    # define the new actual position
                    actual_position[0] = [elements + 1]


class Items:

    def items_drop(structure, position, sprite_size):
        """ Create a random position for items"""
        # Will be used to stop "while"
        counter = 0
        while not counter == 1:
            # randomize a number that can match an index of structure list
            randomizer = random.randrange(0, len(structure))
            # the drop position is equal to the index
            # we randomized so we can check its value
            drop_position = structure[randomizer]
            # if the value is equal to 0
            # it mean that we can use the position to create an item
            if drop_position == 0:
                # will avoid items to have the same position
                structure[drop_position] = "X"
                # the problem is resolved, we can stop the while
                counter = 1
        # here is our item
        return pg.Rect(position[randomizer], sprite_size)
