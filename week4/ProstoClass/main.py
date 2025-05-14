from stack import Stack

if __name__ == "__main__":
    # Создание стека
    stack = Stack()

    # Добавление элементов в стек
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Вывод стека
    print(f"Стек после добавления элементов: {stack}")

    # Удаление элемента из стека
    popped_item = stack.pop()
    print(f"Извлеченный элемент: {popped_item}")
    print(f"Стек после извлечения элемента: {stack}")

    # Просмотр верхнего элемента
    top_item = stack.peek()
    print(f"Верхний элемент стека: {top_item}")

    # Проверка размера стека
    print(f"Размер стека: {stack.size()}")

    # Сохранение стека в файл
    stack.save("stack.json")

    # Загрузка стека из файла
    loaded_stack = Stack.load("stack.json")
    print(f"Загруженный стек: {loaded_stack}")