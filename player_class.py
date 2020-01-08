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
            index for index, values in enumerate(struct) if values == MG_STARTP
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
            return pg.Rect(position[elements], SPRT_SZ)

    def move_up(self, actual_position, structure):
        """ Move the character up if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the top border of the screen
            if (elements - SPRT_NB_WDTH) >= 0:
                # if the upper sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements - SPRT_NB_WDTH] == WALL_TAG:
                    # ...move up !
                    self.move_ip(0, - SPRT_HGT)
                    # define the new actual position
                    actual_position[0] = [elements - SPRT_NB_WDTH]

    def move_down(self, actual_position, structure):
        """ Move the character down if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the bottom border of the screen
            if (elements + SPRT_NB_WDTH) <= (SPRT_NB_WDTH * SPRT_NB_HGT - 1):
                # if the bottom sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements + SPRT_NB_WDTH] == WALL_TAG:
                    # ...move down !
                    self.move_ip(0, SPRT_HGT)
                    # define the new actual position
                    actual_position[0] = [elements + SPRT_NB_WDTH]

    def move_left(self, actual_position, structure, position):
        """ Move the character left if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the left border of the screen
            if not position[elements] <= (SPRT_WDTH, (0-SCRN_HGT)):
                # if the left sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements - 1] == WALL_TAG:
                    # ...move left !
                    self.move_ip(- SPRT_WDTH, 0)
                    # define the new actual position
                    actual_position[0] = [elements - 1]

    def move_right(self, actual_position, structure, position):
        """ Move the character right if possible """
        # getting the actual position value
        for elements in actual_position[0]:
            # check if the player isn't on the right border of the screen
            if not position[elements] >= (SCRN_WDTH - SPRT_WDTH, (0-SCRN_HGT)):
                # if the right sprite isn't a wall
                # (equal 1 in the structure list) :
                if not structure[elements + 1] == WALL_TAG:
                    # ...move right !
                    self.move_ip(SPRT_WDTH, 0)
                    # define the new actual position
                    actual_position[0] = [elements + 1]
