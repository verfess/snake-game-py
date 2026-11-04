"""Проверки преобразования клавиш в команды."""

from snake_game.controls import KeyboardInput

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
PAUSE = "pause"


def test_arrow_keys() -> None:
    assert KeyboardInput._map_key(b"\xe0H") == UP
    assert KeyboardInput._map_key(b"\xe0P") == DOWN
    assert KeyboardInput._map_key(b"\xe0K") == LEFT
    assert KeyboardInput._map_key(b"\xe0M") == RIGHT


def test_arrow_keys_with_alternative_prefix() -> None:
    assert KeyboardInput._map_key(b"\x00H") == UP
    assert KeyboardInput._map_key(b"\x00P") == DOWN


def test_pause_key() -> None:
    assert KeyboardInput._map_key(b"p") == PAUSE
    assert KeyboardInput._map_key(b"P") == PAUSE


def test_unknown_key() -> None:
    assert KeyboardInput._map_key(b"x") is None
    
def test_wasd_keys() -> None:
    assert KeyboardInput._map_key(b"w") == UP
    assert KeyboardInput._map_key(b"s") == DOWN
    assert KeyboardInput._map_key(b"a") == LEFT
    assert KeyboardInput._map_key(b"d") == RIGHT


def test_uppercase_wasd_keys() -> None:
    assert KeyboardInput._map_key(b"W") == UP
    assert KeyboardInput._map_key(b"S") == DOWN
    assert KeyboardInput._map_key(b"A") == LEFT
    assert KeyboardInput._map_key(b"D") == RIGHT
