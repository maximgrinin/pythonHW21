from storage import Storage


# Реализуйте класс Shop. В нем хранится **не больше 5 разных товаров**.
# Shop **не может быть наполнен**, если свободное место закончилось или в нем уже есть 5 разных товаров.
# **Поля:**
# items (словарь название:количество)
# capacity по умолчанию равно 20
# **Методы:**
# `add`(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity
# `remove`(<название>, <количество>) - уменьшает запас items но не ниже 0
# `get_free_space()` - вернуть количество свободных мест
# `get_items()` - возвращает содержание склада в словаре {товар: количество}
# `get_unique_items_count()` - возвращает количество уникальных товаров.
class Shop(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 20

    def __repr__(self):
        return "Магазин"

    def add(self, title: str, quantity: int) -> (bool, str):
        """
        :return: Возвращает два параметра.
        Первый - bool: Логический результат операции добавления товара
        Второй - str: Пояснение, почему результат пополнения неудачный
        """
        # Добавить логику проверки на 5 уникальных товаров
        if not self._check_item(title=title) and self.get_unique_items_count == 5:
            return False, "В магазине превышен лимит уникальных товаров"
        if self._capacity < quantity:
            return False, "В магазине недостаточно места"
        self._items[title] = self._items.get(title, 0) + quantity
        self._capacity -= quantity
        return True, ""

    def remove(self, title: str, quantity: int) -> (bool, str, int):
        """
        :return: Возвращает три параметра.
        Первый - bool: Логический результат операции изъятия товара
        Второй - str: Наименование запрошенного товара
        Третий - int: -1 если товара нет, остаток товара в случае неудачной операции, запрошенное количество в случае удачной
        """
        if not self._check_item(title=title):
            return False, title, -1
        elif self._items[title] < quantity:
            return False, title, self._items[title]
        # quantity = self._check_quantity_limits(title=title, quantity=quantity)
        self._items[title] -= quantity
        self._capacity += quantity
        if self._items[title] == 0:
            del self._items[title]
        return True, title, quantity

    def _check_item(self, title: str) -> bool:
        return title in self._items

    def _check_quantity_limits(self, title: str, quantity: int) -> int:
        current_qnt = self._items[title]
        if current_qnt < quantity:
            quantity = current_qnt
        return quantity

    def get_free_space(self) -> int:
        return self._capacity

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items.keys())

    def state(self):
        return "\nВ магазине хранится:\n" + "\n".join(
            [f"{str(value)} {key}" for key, value in self._items.items()])
