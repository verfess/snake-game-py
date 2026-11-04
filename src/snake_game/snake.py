"""Движок змейки: где она находится, куда ползёт и когда удлиняется."""

from typing import TypeAlias

Position: TypeAlias = tuple[int, int]
DIRECTIONS: frozenset[Position] = frozenset({(0, -1), (0, 1), (-1, 0), (1, 0)})


class Snake:
    """Хранит сегменты змейки и обрабатывает её перемещение по сетке."""

    def __init__(self, start_pos: Position, direction: Position) -> None:
        """Создаёт змейку из одной клетки с заданным направлением."""

        if direction not in DIRECTIONS:
            raise ValueError("Направление должно быть одним из четырёх основных.")

        self.body: list[Position] = [start_pos]
        self.direction: Position = direction
        self._segments_to_add: int = 0

    def head(self) -> Position:
        """Возвращает координаты головы змейки."""
        return self.body[-1]

    def next_head(self, dx: int, dy: int) -> Position:
        """Определяет следующую позицию головы с учётом текущего направления."""

        new_direction = (dx, dy)

        if new_direction not in DIRECTIONS:
            raise ValueError("Движение возможно только на одну клетку по оси.")

        opposite = (-self.direction[0], -self.direction[1])

        if len(self.body) > 1 and new_direction == opposite:
            new_direction = self.direction

        x, y = self.head()
        return (x + new_direction[0], y + new_direction[1])

    def grow(self) -> None:
        """Откладывает удлинение: тело прибавит сегмент на следующем шаге."""
        self._segments_to_add += 1

    def move(self, dx: int, dy: int) -> None:
        """Сдвигает голову на (dx, dy); хвост уходит, если рост не запланирован."""

        new_direction = (dx, dy)

        if new_direction not in DIRECTIONS:
            raise ValueError("Движение возможно только на одну клетку по оси.")

        opposite_direction = (-self.direction[0], -self.direction[1])

        if len(self.body) > 1 and new_direction == opposite_direction:
            dx, dy = self.direction
        else:
            self.direction = new_direction

        x, y = self.head()
        self.body.append((x + dx, y + dy))

        if self._segments_to_add > 0:
            self._segments_to_add -= 1
        else:
            self.body.pop(0)

    def collides_self(self) -> bool:
        """Проверяет оказалась ли голова на клетке, занятой другим сегментом."""
        return self.body.count(self.head()) > 1
