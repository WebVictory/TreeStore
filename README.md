<p><b><u>ЗАДАНИЕ</u></b></p>
<div>Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.<br /><br /><b>Нужно написать класс</b>, который принимает в конструктор массив этих объектов и реализует 4 метода:<br /># - getAll() Должен возвращать изначальный массив элементов.<br /># - getItem(id) Принимает id элемента и возвращает сам объект элемента;<br /># - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,<br /># чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;<br /># - getAllParents(id) Принимает id элемента и возвращает массив из цепочки родительских элементов,<br /># начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,<br /># т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!<br /><br /><b>Требования:</b> максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,<br /># в идеале, прямой доступ к элементам без поиска их в массиве.<br />#<br /><br /># <b>Исходные данные:</b><br />class TreeStore:<br />pass<br /><br /><br />items = [<br />{"id": 1, "parent": "root"},<br />{"id": 2, "parent": 1, "type": "test"},<br />{"id": 3, "parent": 1, "type": "test"},<br />{"id": 4, "parent": 2, "type": "test"},<br />{"id": 5, "parent": 2, "type": "test"},<br />{"id": 6, "parent": 2, "type": "test"},<br />{"id": 7, "parent": 4, "type": None},<br />{"id": 8, "parent": 4, "type": None}<br />]<br />ts = TreeStore(items)<br /><br /># Примеры использования:<br /># - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]<br />#<br /># - ts.getItem(7) // {"id":7,"parent":4,"type":None}<br />#<br /># - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]<br /># - ts.getChildren(5) // []<br />#<br /># - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]</div>

