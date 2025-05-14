from stack import Stack
from stackcollection import StackCollection 

if __name__ == "__main__":
    # Создание стека
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)

    stack2 = Stack()
    stack2.push(3)
    stack2.push(4)

    # Создание контейнера и добавление стеков
    collection = StackCollection()
    collection.add(stack1)
    collection.add(stack2)

    # Вывод контейнера
    print("Контейнер после добавления стеков:")
    print(collection)

    # Удаление стека по индексу
    collection.remove(0)
    print("\nКонтейнер после удаления стека:")
    print(collection)

    # Сохранение контейнера в файл
    collection.save("stack_collection.json")

    # Загрузка контейнера из файла
    loaded_collection = StackCollection.load("stack_collection.json")
    print("\nЗагруженный контейнер:")
    print(loaded_collection)
