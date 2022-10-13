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


# Реализуйте класс Store. В нем хранится любое количество любых товаров.
# Store не может быть заполнен если свободное место закончилось
# **Поля:**
# items (словарь название:количество)
# capacity по умолчанию равно 100
# **Методы:**
# add(<название>, <количество>)  - увеличивает запас items с учетом лимита capacity
# remove(<название>, <количество>) - уменьшает запас items но не ниже 0
# `get_free_space()` - вернуть количество свободных мест
# `get_items()` - возвращает содержание склада в словаре {товар: количество}
# `get_unique_items_count()` - возвращает количество уникальных товаров.
class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def __repr__(self):
        return "Склад"

    def add(self, title: str, quantity: int) -> (bool, str):
        if self._capacity < quantity:
            return False, "На складе недостаточно места"
        self._items[title] = self._items.get(title, 0) + quantity
        self._capacity -= quantity
        return True, ""

    def remove(self, title: str, quantity: int) -> (bool, str, int):
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
        return "\nНа Складе хранится:\n" + "\n".join(
            [f"{str(value)} {key}" for key, value in self._items.items()])


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
        # Добавить логику проверки на 5 уникальных товаров
        if not self._check_item(title=title) and self.get_unique_items_count == 5:
            return False, "В магазине превышен лимит уникальных товаров"
        if self._capacity < quantity:
            return False, "В магазине недостаточно места"
        self._items[title] = self._items.get(title, 0) + quantity
        self._capacity -= quantity
        return True, ""

    def remove(self, title: str, quantity: int) -> (bool, str, int):
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


# Создайте класс Request в котором будет храниться запрос
# `Поля:`
# from - откуда везем (строка)
# to - куда везем (строка)
# amount = 3,
# product = "печеньки" (строка)
# При инициализации принимает список всех складов и строку типа
# **Доставить** 3 печеньки **из** склад **в** магазин
# И возвращает объект класса Request
# from =  "склад",
# to =  "магазин",
# amount = 3,
# product = "печеньки"
class Request:
    def __init__(self, stores: list, req_data: str):
        self._stores = stores
        from_, to_, self._amount, self._product = self._req_data_parse(req_data)
        if from_ == "склад":
            self._from = stores[0]
        elif from_ == "магазин":
            self._from = stores[1]
        else:
            self._from = None

        if to_ == "склад":
            self._to = stores[0]
        elif to_ == "магазин":
            self._to = stores[1]
        else:
            self._to = None

    @staticmethod
    def _req_data_parse(req_data: str) -> (str, str, int, str):
        req_list = req_data.split(" ")
        try:
            req_tulip = (req_list[4].strip().lower(), req_list[6].strip().lower(), int(req_list[1]), req_list[2].strip().lower())
        except Exception:
            req_tulip = ("", "", 0, "")
        return req_tulip

    @property
    def from_(self):
        return self._from

    @property
    def to_(self):
        return self._to

    @property
    def amount(self):
        return self._amount

    @property
    def product(self):
        return self._product


# Напишите функцию main, в которой
# - введите приглашение
# - обрабатывайте ввод пользователя
# - выполните перемещение если это возможно
# - выполните перемещение
if __name__ == '__main__':
    my_store = Store()
    my_shop = Shop()

    # Наполним склад и магазин
    my_store.add(title='печеньки', quantity=6)
    my_store.add(title='собачки', quantity=4)
    my_store.add(title='коробки', quantity=5)
    my_shop.add(title='собачки', quantity=2)
    my_shop.add(title='печеньки', quantity=2)
    print(my_store.state())
    print(my_shop.state())

    is_game_stopped = False
    while not is_game_stopped:
        user_clause = input("\nВведите слово: ")
        if user_clause.strip().lower() == "стоп" or user_clause.strip().lower() == "stop":
            is_game_stopped = True
        else:
            # Создаем запрос на доставку
            my_request = Request([my_store, my_shop], user_clause)
            if my_request.from_ and my_request.to_ and my_request.amount and my_request.product:
                object_from = my_request.from_
                object_to = my_request.to_
                # Пробуем забрать товар для доставки
                result, title, quantity = object_from.remove(title=my_request.product, quantity=my_request.amount)
                if result:
                    print(f"Нужное количество есть в {object_from}")
                    print(f"Курьер забрал {quantity} {title} из {object_from}")
                    print(f"Курьер везет {quantity} {title} из {object_from} в {object_to}")
                    # Пробуем добавить товар куда доставили
                    result_add, _ = object_to.add(title=my_request.product, quantity=my_request.amount)
                    if not result_add:
                        print(f"В {object_to} недостаточно места, попробуйте что-то другое")
                        # Если не получилось - нужно вернуть назад, товар не должен потеряться
                        object_from.add(title=my_request.product, quantity=my_request.amount)
                    else:
                        print(f"Курьер доставил {quantity} {title} в {object_to}")
                elif quantity > 0:
                    print(f"Не хватает в {object_from}, попробуйте заказать меньше")
                else:
                    print(f"Товара нет в {object_from}")
                print(my_store.state())
                print(my_shop.state())
            else:
                print("Не понимаю что нужно сделать")
