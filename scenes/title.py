from constants import COLORS, changeGameState, GAME
import pygame as pg
from system_scripts.ui_elements import Text, Button

title_text = Text("Crash Em Down!", (400, 48), txt_size=80, alignment=0)

play_button = Button(
    "Play", (400, 300), callable=changeGameState, arguments=(GAME), txt_size=64
)


def update(current_time: float, delta_time: float):
    """This is where everything in the scene gets updated."""


def eventHandler(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        play_button.mouseButtonDown(mouse_position=event.pos, mouse_button=event.button)


def draw(canvas: pg.Surface):
    """This is where everything in the scene gets updated."""
    canvas.fill(COLORS["black"])

    title_text.draw(canvas)
    play_button.draw(canvas)
