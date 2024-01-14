from constants import COLORS
import pygame as pg

TexturePlayer1 = pg.image.load("textures/player1.png")

class Player(pg.sprite.Sprite):
    '''Player class'''
    def __init__(self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.original_image = pg.transform.scale(image, (90, 90))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)

player1 = pg.sprite.GroupSingle(Player(TexturePlayer1, 100, 100))

def update(current_time: float, delta_time: float):
    """This is where everything in the scene gets updated."""
    player1.update()


def eventHandler(event):
    pass


def draw(canvas: pg.Surface):
    """This is where everything in the scene gets updated."""
    canvas.fill(COLORS["gray"])
    pg.draw.rect(canvas, COLORS["white"], (50, 50, 700, 500))
    pg.draw.rect(canvas, COLORS["yellow"], (50, 550, 700, 25))

    player1.draw(canvas)
