"""Тесты для проверки движения и роста змейки."""

import pytest

from snake_game.snake import Snake


def test_snake_starts_with_one_segment() -> None:
    """При создании змейка занимает одну клетку."""
    snake = Snake((5, 7), (1, 0))

    assert snake.body == [(5, 7)]
    assert snake.head() == (5, 7)
    assert snake.direction == (1, 0)


def test_snake_moves_forward() -> None:
    """При движении голова перемещается на одну клетку."""
    snake = Snake((3, 4), (1, 0))

    snake.move(1, 0)

    assert snake.body == [(4, 4)]


def test_snake_can_turn() -> None:
    """Змейка меняет направление при повороте."""
    snake = Snake((4, 5), (1, 0))

    snake.move(0, -1)

    assert snake.head() == (4, 4)
    assert snake.direction == (0, -1)


def test_snake_cannot_turn_back() -> None:
    """Змейка продолжает движение, если попытаться развернуть её назад."""
    snake = Snake((3, 4), (1, 0))

    snake.grow()

    snake.move(1, 0)
    snake.move(-1, 0)

    assert snake.body == [(4, 4), (5, 4)]
    assert snake.direction == (1, 0)


def test_snake_grows_after_eating_food() -> None:
    """После роста змейка сохраняет прежний хвост."""
    snake = Snake((2, 3), (1, 0))

    snake.grow()

    snake.move(1, 0)

    assert snake.body == [(2, 3), (3, 3)]


def test_multiple_growth_requests_are_counted() -> None:
    """Несколько запросов на рост увеличивают длину змейки."""
    snake = Snake((1, 2), (1, 0))

    snake.grow()
    snake.grow()

    snake.move(1, 0)
    snake.move(1, 0)

    assert len(snake.body) == 3


def test_snake_stops_growing_after_all_requests() -> None:
    """После выполнения всех запросов на рост длина не увеличивается."""
    snake = Snake((1, 2), (1, 0))
    snake.grow()
    snake.grow()

    snake.move(1, 0)
    snake.move(1, 0)
    snake.move(1, 0)

    assert len(snake.body) == 3


def test_snake_detects_collision_with_itself() -> None:
    """Столкновение головы с другой частью тела обнаруживается."""
    snake = Snake((2, 3), (0, 1))
    snake.body = [(2, 3), (2, 2), (3, 2), (2, 3)]

    assert snake.collides_self()


def test_snake_does_not_collide_without_overlapping() -> None:
    """Если части тела не пересекаются, столкновения нет."""
    snake = Snake((6, 7), (1, 0))

    assert not snake.collides_self()


@pytest.mark.parametrize(
    "direction",
    [(0, 0), (1, 2), (-2, -1), (3, 0)],
)
def test_snake_rejects_invalid_direction(direction: tuple[int, int]) -> None:
    """Нельзя создать змейку с неправильным направлением."""
    with pytest.raises(ValueError):
        Snake((1, 1), direction)


@pytest.mark.parametrize(
    ("dx", "dy"),
    [(0, 0), (1, 2), (-2, -1), (3, 0)],
)
def test_snake_rejects_invalid_move(dx: int, dy: int) -> None:
    """Неправильное движение не должно менять состояние змейки."""
    snake = Snake((4, 5), (1, 0))
    previous_body = snake.body.copy()
    previous_direction = snake.direction

    with pytest.raises(ValueError):
        snake.move(dx, dy)

    assert snake.body == previous_body
    assert snake.direction == previous_direction
