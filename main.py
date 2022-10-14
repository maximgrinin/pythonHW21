from request import Request
from shop import Shop
from store import Store


def print_state(store_obj: Store, shop_obj: Shop):
    print(store_obj.state())
    print(shop_obj.state())


# Напишите функцию main, в которой
# - введите приглашение
# - обрабатывайте ввод пользователя
# - выполните перемещение если это возможно
# - выполните перемещение
if __name__ == '__main__':
    # Создаем экземпляры классов склада и магазина
    my_store = Store()
    my_shop = Shop()

    # Наполним склад и магазин
    my_store.add(title='печеньки', quantity=6)
    my_store.add(title='собачки', quantity=4)
    my_store.add(title='коробки', quantity=5)
    my_shop.add(title='собачки', quantity=2)
    my_shop.add(title='печеньки', quantity=2)
    print_state(my_store, my_shop)

    while True:
        # Ждем команду пользователя
        user_clause = input("\nЧто нужно сделать: ")

        # Обрабатываем окончание перемещений и выходим
        if user_clause.strip().lower() == "стоп" or user_clause.strip().lower() == "stop":
            break

        # Создаем запрос на доставку
        my_request = Request([my_store, my_shop], user_clause)
        # Если не смогли распарсить, сообщаем об этом пользователю и пробуем повторить
        if not all((my_request.from_, my_request.to_, my_request.amount, my_request.product)):
            print("Не понимаю что нужно сделать")
            continue

        # Пробуем забрать товар для доставки
        object_from = my_request.from_
        object_to = my_request.to_
        result, title, quantity = object_from.remove(title=my_request.product, quantity=my_request.amount)
        if not result:
            if quantity > 0:
                print(f"Не хватает в {object_from}, попробуйте заказать меньше")
            else:
                print(f"Товара нет в {object_from}")
            print_state(my_store, my_shop)
            continue
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

        print_state(my_store, my_shop)
