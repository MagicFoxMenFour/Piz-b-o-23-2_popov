import modules.perfomance_analysis as pa
import modules.task_solutions as ts

if __name__ == "__main__":
    # Performance analysis block
    sizes = [100, 1000, 10000, 100000]
    pa.Visualization(sizes)

    # bracket task
    print(ts.bracket_task("{[()]}"))

    # printing task
    orders = {"Отчёт по продажам", "Дипломная работа", "Рецепт пирога"}
    ts.printing_task(orders)

    # palindrome task
    print(ts.palindrome_task("12332"))
