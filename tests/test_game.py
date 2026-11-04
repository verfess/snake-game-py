"""Тесты игровых механик."""

from snake_game.game import FOOD_PER_LEVEL, Game


def test_game_starts_with_food() -> None:
    """В начале игры еда находится на свободной клетке."""
    game = Game(12, 10, 8)

    assert game.food is not None
    assert game.food not in game.snake.body
    assert game.score == 0
    assert not game.is_over


def test_eating_food_increases_score_and_length() -> None:
    """После поедания еды увеличиваются счёт и длина змейки."""
    game = Game(12, 10, 8)
    x, y = game.snake.head()
    game.food = (x + 1, y)

    game.step((1, 0))

    assert game.score == 1
    assert len(game.snake.body) == 2
    assert game.food not in game.snake.body
    assert not game.is_over


def test_hitting_wall_ends_game() -> None:
    """При столкновении со стеной игра заканчивается."""
    game = Game(5, 5, 8)
    game.food = (0, 0)

    for _ in range(3):
        game.step((1, 0))

    assert game.is_over
    assert game.score == 0


def test_hitting_itself_ends_game() -> None:
    """При столкновении головы с телом игра завершается."""
    game = Game(8, 8, 8)
    game.snake.body = [
        (2, 2),
        (2, 3),
        (1, 3),
        (1, 2),
        (0, 2),
    ]
    game.food = (6, 6)

    game.step((1, 0))

    assert game.is_over


def test_level_and_speed_increase() -> None:
    """После FOOD_PER_LEVEL очков повышаются уровень и скорость."""
    game = Game(20, 10, 8)

    for _ in range(FOOD_PER_LEVEL):
        x, y = game.snake.head()
        game.food = (x + 1, y)
        game.step((1, 0))

    assert game.score == FOOD_PER_LEVEL
    assert game.level == 2
    assert game.current_speed == 9


def test_game_ends_when_no_free_cells() -> None:
    """Игра заканчивается, если на поле не осталось свободных клеток."""
    game = Game(1, 1, 8)

    assert game.food is None
    assert game.is_over
