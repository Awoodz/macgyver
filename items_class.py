import pygame as pg
import random
from macgyver_data import *


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
            if drop_position == VOID_TAG:
                # will avoid items to have the same position
                structure[drop_position] = ITEM_TAG
                # the problem is resolved, we can stop the while
                counter = 1
        # here is our item
        return pg.Rect(position[randomizer], sprite_size)
