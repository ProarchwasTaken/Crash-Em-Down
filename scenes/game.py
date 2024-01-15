import pygame.key

from constants import COLORS
import pygame as pg
import copy

TexturePlayer1 = pg.image.load("textures/player1.png")
TexturePlayer2 = pg.image.load("textures/player2.png")

def collisionCheck(sprite, group, type, value):
    dumb = copy.copy(sprite)
    if type == "x":
        dumb.x += value
    if type == "y":
        dumb.y += value
    dumb.dumb = True
    dumb.update()
    return pg.sprite.groupcollide(pg.sprite.GroupSingle(dumb), group, False, False, pg.sprite.collide_mask)

class Wall(pg.sprite.Sprite):
    '''walls'''
    def __init__(self, x, y, sizex, sizey):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((sizex, sizey))
        self.image.fill(COLORS["gray"])
        self.rect = (x, y, sizex, sizey)

class Player(pg.sprite.Sprite):
    '''Player class'''
    def __init__(self, image, x, y, control):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dumb = False
        if control == 0:
            self.up = pg.K_w
            self.down = pg.K_s
            self.left = pg.K_a
            self.right = pg.K_d
        else:
            self.up = pg.K_UP
            self.down = pg.K_DOWN
            self.left = pg.K_LEFT
            self.right = pg.K_RIGHT
        self.jump = True
        self.velocityX = 0
        self.velocityY = 0

        self.delta_time = 0
        self.lerp = 3 #Slipiriness
        self.limit = 500 #Speed limit
        self.speed = 10 #Speed added
        self.gravity = -9 #How fast is gravity
        self.jump_speed = 5 #jumping speed

        self.original_image = pg.transform.scale(image, (90, 90))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pg.mask.from_surface(self.image)

    def move(self):
        if pygame.key.get_pressed()[self.right]:
            if self.velocityX <= self.limit:
                self.velocityX += self.speed * 90 * self.delta_time
        if pygame.key.get_pressed()[self.left]:
            if self.velocityX >= -self.limit:
                self.velocityX -= self.speed * 90 * self.delta_time
        if pygame.key.get_pressed()[self.up] and self.jump:
            self.velocityY += 90 * self.jump_speed
            self.jump = False

    def update(self):
        if not self.dumb:
            change = self.velocityX * self.delta_time
            if not collisionCheck(self, walls, "x", change):
                self.x += change
                self.velocityX = pg.math.Vector2.lerp(pg.math.Vector2(self.velocityX, 0), (0,0), self.lerp * self.delta_time)[0]
            else:
                self.velocityX = 0
            change = self.velocityY * -1 * self.delta_time
            if not collisionCheck(self, walls, "y", change):
                self.y += change
                self.velocityY += 90 * self.gravity * self.delta_time
            else:
                self.velocityY = 0
                self.jump = True
            self.move()

        self.rect.center = (self.x, self.y)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image)

walls = pg.sprite.Group(Wall(0, 0, 50, 600), Wall(750, 0, 50, 600),
                        Wall(0, 0, 800, 50), Wall(0, 550, 800, 50))

player1 = pg.sprite.GroupSingle(Player(TexturePlayer1, 100, 100, 0))
player2 = pg.sprite.GroupSingle(Player(TexturePlayer2, 150, 100, 1))

def update(current_time: float, delta_time: float):
    """This is where everything in the scene gets updated."""
    player1.sprite.delta_time = delta_time
    player2.sprite.delta_time = delta_time

    player1.update()
    player2.update()


def eventHandler(event):
    pass


def draw(canvas: pg.Surface):
    """This is where everything in the scene gets updated."""
    canvas.fill(COLORS["white"])
    walls.draw(canvas)
    pg.draw.rect(canvas, COLORS["yellow"], (50, 550, 700, 25))

    player1.draw(canvas)
    player2.draw(canvas)
