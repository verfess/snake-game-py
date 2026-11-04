"""Обработка нажатий клавиш."""

import msvcrt


class KeyboardInput:
    """Считывает команды игрока с клавиатуры."""

    @staticmethod
    def _map_key(key: bytes) -> str | None:
        """Преобразует код клавиши в игровую команду."""
        keys = {
            b"\xe0H": "up",
            b"\x00H": "up",
            b"\xe0P": "down",
            b"\x00P": "down",
            b"\xe0K": "left",
            b"\x00K": "left",
            b"\xe0M": "right",
            b"\x00M": "right",
        }

        if key in keys:
            return keys[key]
        
        wasd = {
            b"w": "up",
            b"s": "down",
            b"a": "left",
            b"d": "right",
        }

        if key.lower() in wasd:
            return wasd[key.lower()]

        if key.lower() == b"p":
            return "pause"

        return None

    def get_key(self) -> str | None:
        """Возвращает команду или None, если клавиша не нажата."""
        if not msvcrt.kbhit():
            return None

        key = msvcrt.getch()

        if key in (b"\x00", b"\xe0"):
            key += msvcrt.getch()

        return self._map_key(key)
