import pygame as pg
import sys
from constants import RESOLUTION, FPS, gameState, changeGameState, GAME, TITLE
import scenes.title
import scenes.game


def main():
    """This is the main script! Run this first to test the game!"""
    pg.init()

    window = pg.display.set_mode(RESOLUTION)
    pg.display.set_caption("Crash Em Down")

    canvas = pg.Surface(RESOLUTION)

    clock = pg.time.Clock()
    current_time: float = pg.time.get_ticks() / 1000
    prev_time = current_time

    changeGameState(1) #delete this, that's only for testing

    def updateScene(delta_time: float):
        """Updates the scene. What scene is updated depends on the current game state."""
        if gameState() == TITLE:
            scenes.title.update(current_time, delta_time)
        elif gameState() == GAME:
            scenes.game.update(current_time, delta_time)

    def drawScene():
        """Draws the scene. What scene is drawn is based on the current game state."""
        if gameState() == TITLE:
            scenes.title.draw(canvas)
        elif gameState() == GAME:
            scenes.game.draw(canvas)

        window.blit(canvas, (0, 0))
        pg.display.flip()

    # Game loop
    while True:
        clock.tick(FPS)

        current_time: float = pg.time.get_ticks() / 1000
        delta_time: float = current_time - prev_time

        prev_time = current_time

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if gameState() == TITLE:
                scenes.title.eventHandler(event)
            if gameState() == GAME:
                scenes.game.eventHandler(event)

        updateScene(delta_time)
        drawScene()


if __name__ == "__main__":
    main()
