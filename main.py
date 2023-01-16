class TreeStore:
    def __init__(self, items):
        # принимаем массив обьектов
        self.items = items

    def getAll(self):
        """
        Возвращает изначальный массив элементов
        """
        return self.items

    def getItem(self, id):
        """
        Принимает id элемента и возвращает сам объект элемента
        """
        # используем генератор чтобы эффективно работать с данными
        gen = list(item for item in self.items if item["id"] == id)
        # если элемент присутствует возваращаем, первый эдемент списка
        if gen:
            return gen[0]

    def getChildren(self, id):
        """
        Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента

        """
        children = list(item for item in self.items if item["parent"] == id)
        return children

    def __get_parent__(self, item, all=[]):
        """
        приватня рекурсивный метод для получения родительских элементов
        """
        # добавляем в список полученый элемент из вызова функции
        all.append(item)
        # получем родительский id
        parent_id = item["parent"]
        # находим родителя, метод получения обьекта по его id
        new_item = self.getItem(parent_id)
        # условие выхода если закончились элементы, возвращаем полученный список родитлей
        if not new_item:
            return all
        # рекурсивно вызываем себя если обьекты еще есть
        return self.__get_parent__(new_item, all)

    def getAllParents(self, id):
        # находим сам элемнт
        item = self.getItem(id)

        # Перавя версия через рекурсию
        parents = self.__get_parent__(item)

        # Я сделал 2-ю реализациию через цикл
        # эта версия использует цикл зато она проще

        # parents = []
        # while item:
        #     parents.append(item)
        #     parent_id = item["parent"]
        #     item = self.getItem(parent_id)

        # первый элемент обьект для которого находим родителей, убираем его оставляем только родительские
        return parents[1:]


if __name__ == '__main__':
    
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)
    
    #Примеры использования
    get_all = ts.getAll()
    get_item = ts.getItem(7)
    get_children_1 = ts.getChildren(4)
    get_children_2 = ts.getChildren(5)
    get_all_parents = ts.getAllParents(7)

    print(get_all)
    print(get_item)
    print(get_children_1)
    print(get_children_2)
    print(get_all_parents)
