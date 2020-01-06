import pygame as pg
from macgyver_data import *


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
                if not structure[elements - sprt_nb_wdth] == wall_tag:
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
                if not structure[elements + sprt_nb_wdth] == wall_tag:
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
                if not structure[elements - 1] == wall_tag:
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
                if not structure[elements + 1] == wall_tag:
                    # ...move right !
                    self.move_ip(sprt_wdth, 0)
                    # define the new actual position
                    actual_position[0] = [elements + 1]
