"""Логика игры: игровое поле, еда и правила."""

from random import choice

from snake_game.snake import Snake, Position

FOOD_PER_LEVEL = 5
SPEED_INCREMENT = 1


class Game:
    """Хранит состояние игры и управляет её ходом."""

    def __init__(self, width: int, height: int, speed: int) -> None:
        """Создаёт игровое поле и размещает на нём змейку."""

        if width <= 0 or height <= 0 or speed <= 0:
            raise ValueError("Ширина, высота и скорость должны быть положительными.")

        self.width = width
        self.height = height
        self.speed = speed

        start = (width // 2, height // 2)
        self.snake = Snake(start, (1, 0))

        self._score = 0
        self._is_over = False
        self.food: Position | None = self.spawn_food()

    @property
    def score(self) -> int:
        """Возвращает текущий счёт."""
        return self._score

    @property
    def is_over(self) -> bool:
        """Проверяет, закончилась ли игра."""
        return self._is_over

    @property
    def level(self) -> int:
        """Возвращает уровень в зависимости от набранных очков."""
        return self._score // FOOD_PER_LEVEL + 1

    @property
    def current_speed(self) -> int:
        """Вычисляет скорость с учётом текущего уровня."""
        return self.speed + (self.level - 1) * SPEED_INCREMENT

    def spawn_food(self) -> Position | None:
        """Выбирает случайную клетку, не занятую змейкой."""

        free_cells = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if (x, y) not in self.snake.body
        ]

        if not free_cells:
            self._is_over = True
            return None

        return choice(free_cells)

    def step(self, direction: Position) -> None:
        """Выполняет один ход змейки и проверяет результат."""

        if self._is_over:
            return

        next_head = self.snake.next_head(*direction)
        ate_food = next_head == self.food

        if ate_food:
            self.snake.grow()

        self.snake.move(*direction)

        x, y = self.snake.head()

        hit_wall = (
            x < 0
            or x >= self.width
            or y < 0
            or y >= self.height
        )

        if hit_wall or self.snake.collides_self():
            self._is_over = True
            return

        if ate_food:
            self._score += 1
            self.food = self.spawn_food()
