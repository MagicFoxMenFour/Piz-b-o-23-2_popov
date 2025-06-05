#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;

// Базовый абстрактный класс Книга с перегруженными операторами сравнения
class Book {
protected:
    string title;
    string genre;
    string author;
    static int totalCount;

public:
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {
        totalCount++;
    }

    Book(string t, string g, string a) : title(t), genre(g), author(a) {
        totalCount++;
    }

    virtual ~Book() {
        totalCount--;
    }

    // Чисто виртуальная функция
    virtual void displayFullInfo() const = 0;

    // Операторы сравнения (сравниваем по названию)
    bool operator<(const Book& other) const {
        return title < other.title;
    }

    bool operator>(const Book& other) const {
        return title > other.title;
    }

    static int getTotalCount() { return totalCount; }
    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    string getGenre() const { return genre; }
};

int Book::totalCount = 0;

// Класс Основной зал (наследник Book)
class MainHallBook : public Book {
private:
    int shelfNumber;
    bool availableForLoan;

public:
    MainHallBook() : Book(), shelfNumber(0), availableForLoan(true) {}
    MainHallBook(string t, string g, string a, int sn, bool al)
        : Book(t, g, a), shelfNumber(sn), availableForLoan(al) {
    }

    void displayFullInfo() const override {
        cout << "=== Книга основного зала ===" << endl;
        cout << "Название: " << getTitle() << endl;
        cout << "Автор: " << getAuthor() << endl;
        cout << "Жанр: " << getGenre() << endl;
        cout << "Номер полки: " << shelfNumber << endl;
        cout << "Доступна для выноса: " << (availableForLoan ? "Да" : "Нет") << endl;
    }
};

// Класс Читальный зал (наследник Book)
class ReadingRoomBook : public Book {
private:
    int roomNumber;
    string readingTheme;

public:
    ReadingRoomBook() : Book(), roomNumber(0), readingTheme("Неизвестно") {}
    ReadingRoomBook(string t, string g, string a, int rn, string rt)
        : Book(t, g, a), roomNumber(rn), readingTheme(rt) {
    }

    void displayFullInfo() const override {
        cout << "=== Книга читального зала ===" << endl;
        cout << "Название: " << getTitle() << endl;
        cout << "Автор: " << getAuthor() << endl;
        cout << "Жанр: " << getGenre() << endl;
        cout << "Номер читального зала: " << roomNumber << endl;
        cout << "Тематика: " << readingTheme << endl;
    }
};

// Шаблонный класс ArrayContainer
template <typename T>
class ArrayContainer {
private:
    vector<T> elements;

public:
    // Конструктор с заданным размером
    ArrayContainer(size_t n) {
        elements.reserve(n);
    }

    // Добавление элемента
    void addElement(const T& element) {
        elements.push_back(element);
    }

    // Получение элемента по индексу
    T& getElement(size_t index) {
        if (index >= elements.size()) {
            throw out_of_range("Индекс выходит за границы массива");
        }
        return elements[index];
    }

    // Поиск минимального элемента
    T min() const {
        if (elements.empty()) {
            throw logic_error("Массив пуст");
        }
        return *min_element(elements.begin(), elements.end());
    }

    // Поиск максимального элемента
    T max() const {
        if (elements.empty()) {
            throw logic_error("Массив пуст");
        }
        return *max_element(elements.begin(), elements.end());
    }

    // Вывод всех элементов
    void displayAll() const {
        for (const auto& element : elements) {
            cout << element << " ";
        }
        cout << endl;
    }
};

// Специализация для вывода указателей на Book
template <>
void ArrayContainer<Book*>::displayAll() const {
    for (const auto& book : elements) {
        if (book != nullptr) {
            book->displayFullInfo();
            cout << "-------------------" << endl;
        }
    }
}

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 7: ШАБЛОНЫ КЛАССОВ ===" << endl;

    // 1. Шаблон для типа int
    cout << "\n1. Работа с типом int:" << endl;
    ArrayContainer<int> intArray(5);
    intArray.addElement(10);
    intArray.addElement(5);
    intArray.addElement(20);
    intArray.addElement(15);

    cout << "Минимальное значение: " << intArray.min() << endl;
    cout << "Максимальное значение: " << intArray.max() << endl;
    cout << "Все элементы: ";
    intArray.displayAll();

    // 2. Шаблон для типа char
    cout << "\n2. Работа с типом char:" << endl;
    ArrayContainer<char> charArray(3);
    charArray.addElement('z');
    charArray.addElement('a');
    charArray.addElement('m');

    cout << "Минимальное значение: " << charArray.min() << endl;
    cout << "Максимальное значение: " << charArray.max() << endl;
    cout << "Все элементы: ";
    charArray.displayAll();

    // 3. Шаблон для указателей на Book
    cout << "\n3. Работа с указателями на Book:" << endl;
    ArrayContainer<Book*> bookPtrArray(3);

    MainHallBook book1("Преступление и наказание", "Роман", "Достоевский", 15, true);
    ReadingRoomBook book2("Война и мир", "Роман-эпопея", "Толстой", 3, "Историческая литература");
    MainHallBook book3("Анна Каренина", "Роман", "Толстой", 22, false);

    bookPtrArray.addElement(&book1);
    bookPtrArray.addElement(&book2);
    bookPtrArray.addElement(&book3);

    cout << "Минимальная книга (по названию):" << endl;
    bookPtrArray.min()->displayFullInfo();
    cout << "\nМаксимальная книга (по названию):" << endl;
    bookPtrArray.max()->displayFullInfo();
    cout << "\nВсе книги:" << endl;
    bookPtrArray.displayAll();

    // 4. Шаблон для MainHallBook
    cout << "\n4. Работа с MainHallBook:" << endl;
    ArrayContainer<MainHallBook> mainHallArray(2);

    MainHallBook mh1("Идиот", "Роман", "Достоевский", 12, true);
    MainHallBook mh2("Братья Карамазовы", "Роман", "Достоевский", 18, false);

    mainHallArray.addElement(mh1);
    mainHallArray.addElement(mh2);

    cout << "Минимальная книга (по названию):" << endl;
    mainHallArray.min().displayFullInfo();
    cout << "\nМаксимальная книга (по названию):" << endl;
    mainHallArray.max().displayFullInfo();

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}