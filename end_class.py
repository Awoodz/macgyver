import pygame as pg
import time


def end(scrn, end_img, end_sound):
    """Display end screen then close the game"""
    # display end screen
    scrn.blit(end_img, (0, 0))
    pg.display.update()
    # play end sound
    end_sound.play()
    # freeze the game during 2 sec
    time.sleep(2)
    # then quit
    quit()
