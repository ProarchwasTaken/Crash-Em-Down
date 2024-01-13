import pygame as pg
import sys
from constants import RESOLUTION, FPS, COLORS


def main():
    """This is the main script! Run this first to test the game!"""
    pg.init()

    window = pg.display.set_mode(RESOLUTION)
    pg.display.set_caption("Crash Em Down")

    canvas = pg.Surface(RESOLUTION)

    clock = pg.time.Clock()
    current_time: float = pg.time.get_ticks() / 1000
    prev_time = current_time

    def updateScene():
        """This is where everything in the scene gets updated."""
        pass

    def drawScene():
        """This is where everything in the scene gets updated."""
        canvas.fill(COLORS["gray"])
        pg.draw.rect(canvas, COLORS["white"], (50,50, 700,500))
        pg.draw.rect(canvas, COLORS["yellow"], (50,550, 700,25))

        window.blit(canvas, (0, 0))
        pg.display.flip()

    # Game loop
    while True:
        clock.tick(FPS)

        current_time: float = pg.time.get_ticks() / 1000
        deltatime: float = current_time - prev_time

        prev_time = current_time

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        updateScene()
        drawScene()


if __name__ == "__main__":
    main()
