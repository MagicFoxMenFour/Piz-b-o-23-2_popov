#include <iostream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

// Абстрактный базовый класс Книга
class Book {
protected:
    string title;
    string genre;
    string author;

public:
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {
        cout << "Вызван конструктор без параметров класса Book" << endl;
    }

    Book(string t, string g, string a) : title(t), genre(g), author(a) {
        cout << "Вызван конструктор с параметрами класса Book: " << title << endl;
    }

    virtual ~Book() {
        cout << "Вызван деструктор класса Book: " << title << endl;
    }

    // Чисто виртуальная функция (делаем класс абстрактным)
    virtual void displayFullInfo() const = 0;

    string getTitle() const { return title; }
};

// Класс Основной зал (наследник Book)
class MainHallBook : public Book {
private:
    int shelfNumber;
    bool availableForLoan;

public:
    MainHallBook() : Book(), shelfNumber(0), availableForLoan(true) {
        cout << "Вызван конструктор без параметров класса MainHallBook" << endl;
    }

    MainHallBook(string t, string g, string a, int sn, bool al)
        : Book(t, g, a), shelfNumber(sn), availableForLoan(al) {
        cout << "Вызван конструктор с параметрами класса MainHallBook: " << title << endl;
    }

    ~MainHallBook() override {
        cout << "Вызван деструктор класса MainHallBook: " << title << endl;
    }

    void displayFullInfo() const override {
        cout << "=== Книга основного зала ===" << endl;
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
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
    ReadingRoomBook() : Book(), roomNumber(0), readingTheme("Неизвестно") {
        cout << "Вызван конструктор без параметров класса ReadingRoomBook" << endl;
    }

    ReadingRoomBook(string t, string g, string a, int rn, string rt)
        : Book(t, g, a), roomNumber(rn), readingTheme(rt) {
        cout << "Вызван конструктор с параметрами класса ReadingRoomBook: " << title << endl;
    }

    ~ReadingRoomBook() override {
        cout << "Вызван деструктор класса ReadingRoomBook: " << title << endl;
    }

    void displayFullInfo() const override {
        cout << "=== Книга читального зала ===" << endl;
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
        cout << "Номер читального зала: " << roomNumber << endl;
        cout << "Тематика: " << readingTheme << endl;
    }
};

// Класс Библиотека (модифицированный)
class Library {
private:
    string name;
    string address;
    vector<unique_ptr<Book>> books; // Используем умные указатели для полиморфизма

public:
    Library(string n, string a) : name(n), address(a) {
        cout << "Вызван конструктор класса Library: " << name << endl;
    }

    ~Library() {
        cout << "Вызван деструктор класса Library: " << name << endl;
    }

    // Добавление книги (полиморфное)
    template<typename T, typename... Args>
    void addBook(Args&&... args) {
        books.emplace_back(make_unique<T>(forward<Args>(args)...));
        cout << "Добавлена книга: " << books.back()->getTitle() << endl;
    }

    // Вывод информации о библиотеке и всех книгах
    void displayAll() const {
        cout << "\n=== Информация о библиотеке ===" << endl;
        cout << "Название: " << name << endl;
        cout << "Адрес: " << address << endl;
        cout << "Количество книг: " << books.size() << endl;

        if (!books.empty()) {
            cout << "\n=== Список книг ===" << endl;
            for (const auto& book : books) {
                book->displayFullInfo();
                cout << "-------------------" << endl;
            }
        }
    }
};

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 4: АБСТРАКТНЫЕ КЛАССЫ И ПОЛИМОРФИЗМ ===" << endl;

    // 1. Создание массива указателей на базовый класс
    cout << "\n1. Массив указателей на базовый класс (Book*):" << endl;
    const int ARRAY_SIZE = 3;
    Book* books[ARRAY_SIZE];

    books[0] = new MainHallBook("Преступление и наказание", "Роман", "Достоевский", 15, true);
    books[1] = new ReadingRoomBook("Война и мир", "Роман-эпопея", "Толстой", 3, "Историческая литература");
    books[2] = new MainHallBook("Анна Каренина", "Роман", "Толстой", 22, false);

    cout << "\nВывод содержимого массива Book*:" << endl;
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        books[i]->displayFullInfo();
        cout << "-------------------" << endl;
    }

    // Очистка памяти
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        delete books[i];
    }

    // 2. Работа с модифицированным классом Library
    cout << "\n2. Демонстрация работы с классом Library:" << endl;
    Library lib("Центральная городская библиотека", "ул. Ленина, 10");

    // Добавляем книги разных типов
    lib.addBook<MainHallBook>("Мастер и Маргарита", "Роман", "Булгаков", 12, true);
    lib.addBook<ReadingRoomBook>("Братья Карамазовы", "Роман", "Достоевский", 5, "Философская литература");
    lib.addBook<MainHallBook>("Идиот", "Роман", "Достоевский", 18, false);

    // Выводим всю информацию о библиотеке
    lib.displayAll();

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}