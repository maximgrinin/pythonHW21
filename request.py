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
        """
        :return: Возвращает четыре параметра.
        Первый - str: Наименование объекта откуда перемещаем товар
        Второй - str: Наименование объекта куда пересещаем товар
        Третий - int: Количество перемещаемого товара
        Четвертый - str: Наименование перемещаемого товара
        """
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
