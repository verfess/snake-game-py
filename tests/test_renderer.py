"""Проверки отображения отдельных клеток."""

from snake_game.renderer import Renderer

HEAD = Renderer.HEAD
BODY = Renderer.BODY
FOOD = Renderer.FOOD
EMPTY = Renderer.EMPTY


def test_cell_displays_head() -> None:
    assert Renderer._cell((3, 3), (3, 3), (5, 5), {(3, 3)}) == HEAD


def test_cell_displays_food() -> None:
    assert Renderer._cell((5, 5), (3, 3), (5, 5), {(3, 3)}) == FOOD


def test_cell_displays_body() -> None:
    assert Renderer._cell((4, 3), (3, 3), (5, 5), {(3, 3), (4, 3)}) == BODY


def test_cell_displays_empty_cell() -> None:
    assert Renderer._cell((2, 2), (3, 3), (5, 5), {(3, 3)}) == EMPTY
