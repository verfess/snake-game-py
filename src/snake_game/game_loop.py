"""Запуск игрового процесса."""

import time

from snake_game.controls import KeyboardInput
from snake_game.game import Game
from snake_game.renderer import Renderer
from snake_game.snake import Position

KEY_DIRECTIONS: dict[str, Position] = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


class GameLoop:
    """Объединяет управление, ход игры и вывод поля."""

    def __init__(
        self,
        game: Game,
        renderer: Renderer,
        keyboard: KeyboardInput,
    ) -> None:
        """Сохраняет объекты, нужные для запуска."""
        self.game = game
        self.renderer = renderer
        self.keyboard = keyboard

    def run(self) -> None:
        """Запускает новые раунды по запросу игрока."""
        while True:
            self._run_round()
            self.renderer.render_game_over(self.game)

            while True:
                answer = input().strip().lower()
                if answer in ("y", "n"):
                    break
                print("Введите y или n.")

            if answer == "n":
                break

            self.game = Game(
                self.game.width,
                self.game.height,
                self.game.speed,
            )

    def _run_round(self) -> None:
        """Выполняет раунд до столкновения."""
        is_pause = False
        self.renderer.render(self.game)

        while not self.game.is_over:
            key = self.keyboard.get_key()

            if key == "pause":
                is_pause = not is_pause
                self.renderer.render(self.game, is_pause=is_pause)

            elif is_pause:
                time.sleep(0.05)
                continue

            else:
                direction = (
                    KEY_DIRECTIONS.get(key, self.game.snake.direction)
                    if key is not None
                    else self.game.snake.direction
                )

                self.game.step(direction)
                self.renderer.render(self.game)

                time.sleep(1 / self.game.current_speed)
