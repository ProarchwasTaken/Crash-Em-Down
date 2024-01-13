from constants import COLORS
import pygame as pg


def update(current_time: float, delta_time: float):
    """This is where everything in the scene gets updated."""
    pass


def eventHandler(event):
    pass


def draw(canvas: pg.Surface):
    """This is where everything in the scene gets updated."""
    canvas.fill(COLORS["gray"])
    pg.draw.rect(canvas, COLORS["white"], (50, 50, 700, 500))
    pg.draw.rect(canvas, COLORS["yellow"], (50, 550, 700, 25))
