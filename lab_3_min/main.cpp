#include <iostream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

// Базовый класс Книга
class Book {
protected:
    string title;
    string genre;
    string author;

public:
    // Конструкторы и деструктор
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {
        cout << "Вызван конструктор без параметров класса Book" << endl;
    }

    Book(string t, string g, string a) : title(t), genre(g), author(a) {
        cout << "Вызван конструктор с параметрами класса Book: " << title << endl;
    }

    Book(const Book& other) : title(other.title), genre(other.genre), author(other.author) {
        cout << "Вызван конструктор копирования класса Book: " << title << endl;
    }

    virtual ~Book() {
        cout << "Вызван деструктор класса Book: " << title << endl;
    }

    // Методы ввода/вывода
    virtual void input() {
        cout << "Введите название книги: ";
        getline(cin, title);
        cout << "Введите жанр: ";
        getline(cin, genre);
        cout << "Введите автора: ";
        getline(cin, author);
    }

    virtual void display() const {
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
    }

    string getTitle() const { return title; }
};

// Класс Основной зал (наследник Book)
class MainHallBook : public Book {
private:
    int shelfNumber;
    bool availableForLoan;

public:
    // Конструкторы и деструктор
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

    // Методы ввода/вывода
    void input() override {
        Book::input();
        cout << "Введите номер полки: ";
        cin >> shelfNumber;
        cout << "Доступна для выноса (1 - да, 0 - нет): ";
        cin >> availableForLoan;
        cin.ignore();
    }

    void display() const override {
        Book::display();
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
    // Конструкторы и деструктор
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

    // Методы ввода/вывода
    void input() override {
        Book::input();
        cout << "Введите номер читального зала: ";
        cin >> roomNumber;
        cin.ignore();
        cout << "Введите тематику: ";
        getline(cin, readingTheme);
    }

    void display() const override {
        Book::display();
        cout << "Номер читального зала: " << roomNumber << endl;
        cout << "Тематика: " << readingTheme << endl;
    }
};

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 3: НАСЛЕДОВАНИЕ ===" << endl;

    // 1. Создание объектов базового класса и классов-наследников
    cout << "\n1. Создание отдельных объектов:" << endl;

    cout << "\nСоздание базового объекта Book:" << endl;
    Book book1("1984", "Антиутопия", "Джордж Оруэлл");
    book1.display();

    cout << "\nСоздание объекта MainHallBook:" << endl;
    MainHallBook mhBook("Преступление и наказание", "Роман", "Достоевский", 15, true);
    mhBook.display();

    cout << "\nСоздание объекта ReadingRoomBook:" << endl;
    ReadingRoomBook rrBook("Война и мир", "Роман-эпопея", "Толстой", 3, "Историческая литература");
    rrBook.display();

    // 2. Создание массива указателей на базовый класс
    cout << "\n2. Массив указателей на базовый класс (Book*):" << endl;
    const int ARRAY_SIZE = 4;
    Book* books[ARRAY_SIZE];

    books[0] = new Book("Мастер и Маргарита", "Роман", "Булгаков");
    books[1] = new MainHallBook("Анна Каренина", "Роман", "Толстой", 22, false);
    books[2] = new ReadingRoomBook("Братья Карамазовы", "Роман", "Достоевский", 5, "Философская литература");
    books[3] = new MainHallBook("Идиот", "Роман", "Достоевский", 18, true);

    cout << "\nВывод содержимого массива Book*:" << endl;
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        books[i]->display();
        cout << "-------------------" << endl;
    }

    // Очистка памяти
    for (int i = 0; i < ARRAY_SIZE; ++i) {
        delete books[i];
    }

    // 3. Создание массива объектов класса-наследника
    cout << "\n3. Массив объектов MainHallBook:" << endl;
    MainHallBook mainHallBooks[2];

    cout << "\nВвод данных для массива MainHallBook:" << endl;
    for (int i = 0; i < 2; ++i) {
        cout << "\nКнига " << i + 1 << ":" << endl;
        mainHallBooks[i].input();
    }

    cout << "\nВывод содержимого массива MainHallBook:" << endl;
    for (int i = 0; i < 2; ++i) {
        mainHallBooks[i].display();
        cout << "-------------------" << endl;
    }

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}