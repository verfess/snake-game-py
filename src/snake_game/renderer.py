"""Обновляет игровое поле и строку показателей."""

from snake_game.game import Game
from snake_game.snake import Position


class Renderer:
    """Показывает состояние игры в терминале."""

    HEAD = "@"
    BODY = "o"
    FOOD = "*"
    EMPTY = " "
    WALL_HORIZONTAL = "-"
    WALL_VERTICAL = "|"
    CORNER = "+"

    @staticmethod
    def _cell(
        position: Position,
        head: Position,
        food: Position | None,
        body: set[Position],
    ) -> str:
        """Возвращает символ для указанной клетки."""
        if position == head:
            return Renderer.HEAD
        if position == food:
            return Renderer.FOOD
        if position in body:
            return Renderer.BODY
        return Renderer.EMPTY

    def render(self, game: Game, is_pause: bool = False) -> None:
        """Рисует поле и текущие показатели игры."""
        head = game.snake.head()
        body = set(game.snake.body)

        field = [
            self.WALL_VERTICAL
            + "".join(
                self._cell((x, y), head, game.food, body) for x in range(game.width)
            )
            + self.WALL_VERTICAL
            for y in range(game.height)
        ]

        border = self.CORNER + self.WALL_HORIZONTAL * game.width + self.CORNER

        output = [
            border,
            *field,
            border,
            f"Счёт: {game.score}",
            f"Уровень: {game.level}",
            f"Скорость: {game.current_speed}",
        ]

        if is_pause:
            output.append("ПАУЗА — нажми P, чтобы продолжить")

        screen = "\033[H" + "\r\n".join(
            line + "\033[K" for line in output
        ) + "\033[J"

        print(screen, end="", flush=True)

    def render_game_over(self, game: Game) -> None:
        """Показывает итоговый счёт и предложение сыграть ещё раз."""
        output = [
            "",
            "ИГРА ОКОНЧЕНА",
            f"Итоговый счёт: {game.score}",
            "",
            "Сыграть ещё раз? (y/n)",
        ]
        print("\033[H" + "\r\n".join(output), end="", flush=True)
