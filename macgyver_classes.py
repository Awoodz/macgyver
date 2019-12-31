import pygame as pg
import random
from macgyver_data import *

class Level:

    def generate(self):
        """Convert the txt file into an array named "maze" """
        with open("level1.txt") as level_file:
            for line in level_file:
                level_lines = [] 
                for sprite in line:
                    if sprite == '0':
                        sprite = int(sprite) # the code need numbers to be int format
                    if sprite == '1':
                        sprite = int(sprite) # the code need numbers to be int format            
                    if sprite != '\n':
                        level_lines.append(sprite)
                self.append(level_lines)

        

    def level_structure(maze, structure, position, key_position): 
        """ From the generated array, will create a list of every sprite in the array and a dictionnary of every position on screen """      
        for j, line in enumerate(maze):
            for i, case in enumerate(line):
                structure.append(case)
                position[key_position] = (i*sprite_width, j*sprite_height) # Keys in position dictionnary will be the same that the indexes of the structure list.
                key_position = key_position + 1

    def draw_wall(surface, wall_structure, position):
        """ Display walls on the screen """
        for elements in wall_structure :
            screen.blit(wall_img, position[elements])

class Player:

    def __init__(self, actual_position, structure, position):
        """find the starting position + define the start position as actual position (only at initialization)"""
        start_position = [index for index, values in enumerate(structure) if values == macgyver_start_point] # Search for the index in structure list that is equal to the macgyver start point caracter and create a list with all those index
        if start_position == []: # avoid a bug when start point is upper left corner...
            start_position.append(0) # ...giving it a value = 0
        actual_position.append(start_position)

    def rect_entity(structure, position, entity_start_point):
        """create rect for entities such as macgyver or the guardian"""
        entity = [index for index, values in enumerate(structure) if values == entity_start_point] # Search for the index in structure list that is equal to the entity start point caracter and create a list with all those index
        for elements in entity:
            return pg.Rect(position[elements], sprite_size)

    def move_up(self, actual_position, structure):
        """ Move the character up if possible """
        for elements in actual_position[0]: # getting the actual position value
            if (elements - sprite_nb_width) >= 0: # check if the player isn't on the top border of the screen
                if not structure[elements - sprite_nb_width] == 1: # if the upper sprite isn't a wall (equal 1 in the structure list) :
                    self.move_ip(0, - sprite_height) # ...move up !
                    actual_position[0] = [elements - sprite_nb_width] # define the new actual position

    def move_down(self, actual_position, structure):
        """ Move the character down if possible """
        for elements in actual_position[0]: # getting the actual position value
            if (elements + sprite_nb_width) <= (sprite_nb_width * sprite_nb_height - 1): # check if the player isn't on the bottom border of the screen
                if not structure[elements + sprite_nb_width] == 1: # if the bottom sprite isn't a wall (equal 1 in the structure list) :
                    self.move_ip(0, sprite_height) # ...move down !
                    actual_position[0] = [elements + sprite_nb_width] # define the new actual position

    def move_left(self, actual_position, structure, position):
        """ Move the character left if possible """
        for elements in actual_position[0]: # getting the actual position value
            if not position[elements] <= (sprite_width, (0-screen_height)): # check if the player isn't on the left border of the screen
                if not structure[elements - 1] == 1: # if the left sprite isn't a wall (equal 1 in the structure list) :
                    self.move_ip(- sprite_width, 0) # ...move left !
                    actual_position[0] = [elements - 1] # define the new actual position
        

    def move_right(self, actual_position, structure, position):
        """ Move the character right if possible """
        for elements in actual_position[0]: # getting the actual position value
            if not position[elements] >= (screen_width - sprite_width, (0-screen_height)): # check if the player isn't on the right border of the screen
                if not structure[elements + 1] == 1: # if the right sprite isn't a wall (equal 1 in the structure list) :
                    self.move_ip(sprite_width, 0) # ...move right !
                    actual_position[0] = [elements + 1] # define the new actual position
                    
# items
class Items:

    def items_drop(structure, position, sprite_size):
        counter = 0
        while not counter == 1:
            randomizer = random.randrange(0, len(structure))            
            drop_position = structure[randomizer]           
            if drop_position == 0:               
                structure[drop_position] = "X"
                counter = 1    
        return pg.Rect(position[randomizer], sprite_size)