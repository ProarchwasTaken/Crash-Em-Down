import pygame as pg
from constants import COLORS, TARGET_FPS


class Player:
    sprite_player1 = pg.image.load("textures/player1.png").convert()
    sprite_player1.set_colorkey(COLORS["transparent"])

    sprite_player2 = pg.image.load("textures/player2.png").convert()
    sprite_player2.set_colorkey(COLORS["transparent"])

    def __init__(self) -> None:
        pass
