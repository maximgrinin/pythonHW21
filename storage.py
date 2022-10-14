from abc import ABC, abstractmethod


# Создайте абстрактный класс Storage
# **Поля:**
# `items` (словарь название:количество)
# `capacity` (целое число)
# **Методы:**
# `add`(<название>, <количество>)  - увеличивает запас items
# `remove`(<название>, <количество>) - уменьшает запас items
# `get_free_space()` - вернуть количество свободных мест
# `get_items()` - возвращает сожержание склада в словаре {товар: количество}
# `get_unique_items_count()` - возвращает количество уникальных товаров.
class Storage(ABC):
    def __int__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, title: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int):
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """:return: вернуть количество свободных мест"""

    @abstractmethod
    def get_items(self) -> dict:
        """:return: возвращает сожержание склада в словаре {товар: количество}"""

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """:return: возвращает количество уникальных товаров"""
