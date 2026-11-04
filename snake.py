"""Запуск консольной игры «Змейка»."""

import argparse

from snake_game.controls import KeyboardInput
from snake_game.game import Game
from snake_game.game_loop import GameLoop
from snake_game.renderer import Renderer


def positive_int(value: str) -> int:
    """Проверяет, что переданное значение является положительным числом."""
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Значение должно быть больше нуля.")
    return number


def main() -> None:
    """Обрабатывает параметры запуска и запускает игру."""
    parser = argparse.ArgumentParser(description="Консольная игра «Змейка».")
    parser.add_argument("--width", type=positive_int, default=20, help="Ширина поля")
    parser.add_argument("--height", type=positive_int, default=15, help="Высота поля")
    parser.add_argument("--speed", type=positive_int, default=8, help="Скорость игры")

    args = parser.parse_args()

    game = Game(args.width, args.height, args.speed)
    renderer = Renderer()
    keyboard = KeyboardInput()

    game_loop = GameLoop(game, renderer, keyboard)
    game_loop.run()


if __name__ == "__main__":
    main()
