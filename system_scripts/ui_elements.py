from types import NoneType
from typing import Any, Callable, Optional
import pygame as pg
from constants import COLORS


class Text:
    """This class is for creating text of all different colors, fonts, alignment, positions etc. Each instance comes
    equiped with a method that changes it's position and alignment, and a method for drawing the text onto the screen
    """

    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        txt_size: int = 32,
        txt_color: tuple[int, int, int] = COLORS["white"],
        txt_bgColor: NoneType | tuple[int, int, int] = None,
        font=None,
        alignment: int = 1,
    ):
        font = pg.font.Font(font, txt_size)

        self.text: pg.Surface = font.render(text, True, txt_color, txt_bgColor)

        self.position: tuple = 0, 0
        self.setPosition(position, alignment)

    def setPosition(self, new_position: tuple[int, int], alignment: int):
        """Changes the position of the text. You can also set the text's alignment. With '1' meaning: left aligned, '0'
        meaning centered aligned, and '-1' meaning right aligned. If any other valuer were to be used, an error will be
        raised."""

        txt_width: int = self.text.get_width()
        new_x, new_y = new_position

        LEFT: int = 1
        CENTER: int = 0
        RIGHT: int = -1

        if alignment == LEFT:
            self.position = new_position

        elif alignment == CENTER:
            new_x -= txt_width / 2
            self.position = new_x, new_y

        elif alignment == -RIGHT:
            new_x -= txt_width
            self.position = new_x, new_y

        else:
            raise ValueError(
                "You can only use integers ranging from -1 to 1 when setting alignment!"
            )

    def draw(self, canvas: pg.Surface):
        canvas.blit(self.text, self.position)


class Button(Text):
    """Class that's used for creating buttons that call a function or method when clicked. Subclasses the Text class.
    On initialization, you'll have to assign a button a method or function and the arguments required to call that
    function."""

    def __init__(
        self,
        text: str,
        position: tuple[int, int],
        callable: Callable,
        arguments=tuple(),
        txt_size: int = 32,
        txt_color: tuple[int, int, int] = COLORS["black"],
        txt_bgColor: tuple[int, int, int] = COLORS["white"],
        font=None,
        alignment: int = 0,
    ):
        super().__init__(
            text, position, txt_size, txt_color, txt_bgColor, font, alignment
        )

        self.rect = pg.Rect((self.position), self.text.get_size())
        self.btn_callable = callable
        self.btn_arguments = arguments

    def mouseButtonDown(self, mouse_position: tuple, mouse_button: int):
        """Called when the scene that the button is in detects a press of the mouse button. If the button pressed was
        the left mouse button, and the position of the mouse is inside the button's rect, then function or method that
        was assigned to the button will be called."""

        if mouse_button == 1 and self.rect.collidepoint(mouse_position):
            self.btn_callable(self.btn_arguments)
