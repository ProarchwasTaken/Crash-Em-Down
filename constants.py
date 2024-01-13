WIDTH: int = 800
HEIGHT: int = 600

RESOLUTION: tuple = (WIDTH, HEIGHT)

FPS: int = 60
TARGET_FPS = FPS

COLORS: dict = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (75, 75, 75),
    "yellow": (255, 255, 0),
}

_game_state: bool = False


def gameState() -> bool:
    """Most important variable in the game. Determines what state the game should be in and wether it should be in the
    title scene, or the game scene. This function returns the value of _game_state and it must be called instead of
    checking the variable directly."""
    return _game_state


def changeGameState(value: bool):
    """This function must be called in order to change the _game_state variable."""
    global _game_state
    _game_state = value
