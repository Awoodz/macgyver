import random
from macgyver_data import *


class Level:

    def generate(self):
        """Convert the txt level file into an array"""
        # open a random maze file
        with open(random.choice(level_choice)) as level_file:
            for line in level_file:
                level_lines = []
                for sprite in line:
                    # check if the string is a number
                    try:
                        # if yes, convert it to int instead of string
                        sprite = int(sprite)
                        # else, pass
                    except ValueError:
                        pass
                    # check if there is a line break
                    if sprite != '\n':
                        level_lines.append(sprite)
                self.append(level_lines)

    def level_structure(maze, structure, position):
        """ From the generated array, will create a list of every sprite
        in the array and a dictionnary of every position on screen """
        # will be used to determine keys in the position dictionnary
        key_position = 0
        for j, line in enumerate(maze):
            for i, case in enumerate(line):
                structure.append(case)
                # Keys in position dictionnary will be the same
                # that the indexes of the structure list.
                position[key_position] = (i*sprt_wdth, j*sprt_hgt)
                key_position = key_position + 1

    def draw_level(surface, level_structure, position, img):
        """ Display walls or floor on the screen """
        for elements in level_structure:
            surface.blit(img, position[elements])
