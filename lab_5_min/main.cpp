#include <iostream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

// Абстрактный базовый класс Книга
class Book {
protected:  // Изменено с private на protected для доступа в производных классах
    string title;
    string genre;
    string author;
    static int totalCount; // Статический счетчик объектов

public:
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {
        totalCount++;
        cout << "Вызван конструктор без параметров класса Book (всего объектов: " << totalCount << ")" << endl;
    }

    Book(string t, string g, string a) : title(t), genre(g), author(a) {
        totalCount++;
        cout << "Вызван конструктор с параметрами класса Book: " << title << " (всего объектов: " << totalCount << ")" << endl;
    }

    virtual ~Book() {
        totalCount--;
        cout << "Вызван деструктор класса Book: " << title << " (осталось объектов: " << totalCount << ")" << endl;
    }

    // Чисто виртуальная функция
    virtual void displayFullInfo() const = 0;

    // Статический метод для получения количества объектов
    static int getTotalCount() {
        return totalCount;
    }

    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    string getGenre() const { return genre; }
};

// Инициализация статической переменной
int Book::totalCount = 0;

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
        cout << "Вызван конструктор с параметрами класса MainHallBook: " << getTitle() << endl;
    }

    ~MainHallBook() override {
        cout << "Вызван деструктор класса MainHallBook: " << getTitle() << endl;
    }

    void displayFullInfo() const override {
        cout << "=== Книга основного зала ===" << endl;
        cout << "Название: " << getTitle() << endl;
        cout << "Автор: " << getAuthor() << endl;  // Используем getter вместо прямого доступа
        cout << "Жанр: " << getGenre() << endl;    // Используем getter вместо прямого доступа
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
        cout << "Вызван конструктор с параметрами класса ReadingRoomBook: " << getTitle() << endl;
    }

    ~ReadingRoomBook() override {
        cout << "Вызван деструктор класса ReadingRoomBook: " << getTitle() << endl;
    }

    void displayFullInfo() const override {
        cout << "=== Книга читального зала ===" << endl;
        cout << "Название: " << getTitle() << endl;
        cout << "Автор: " << getAuthor() << endl;  // Используем getter вместо прямого доступа
        cout << "Жанр: " << getGenre() << endl;    // Используем getter вместо прямого доступа
        cout << "Номер читального зала: " << roomNumber << endl;
        cout << "Тематика: " << readingTheme << endl;
    }
};


// Класс Библиотека (модифицированный)
class Library {
private:
    string name;
    string address;
    vector<unique_ptr<Book>> books;
    static int booksInLibrariesCount; // Счетчик книг во всех библиотеках

public:
    Library(string n, string a) : name(n), address(a) {
        cout << "Вызван конструктор класса Library: " << name << endl;
    }

    ~Library() {
        cout << "Вызван деструктор класса Library: " << name << endl;
    }

    // Добавление книги
    template<typename T, typename... Args>
    void addBook(Args&&... args) {
        books.emplace_back(make_unique<T>(forward<Args>(args)...));
        booksInLibrariesCount++;
        cout << "Добавлена книга: " << books.back()->getTitle()
            << " (всего книг в библиотеках: " << booksInLibrariesCount << ")" << endl;
    }

    // Удаление книги
    void removeBook(int index) {
        if (index >= 0 && index < books.size()) {
            cout << "Удалена книга: " << books[index]->getTitle()
                << " (осталось книг в библиотеках: " << booksInLibrariesCount - 1 << ")" << endl;
            books.erase(books.begin() + index);
            booksInLibrariesCount--;
        }
    }

    // Вывод информации о библиотеке
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

    // Статический метод для получения количества книг во всех библиотеках
    static int getBooksInLibrariesCount() {
        return booksInLibrariesCount;
    }
};

// Инициализация статической переменной
int Library::booksInLibrariesCount = 0;

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 5: СТАТИЧЕСКИЕ ЧЛЕНЫ КЛАССА ===" << endl;

    // 1. Вывод количества объектов до их создания
    cout << "\n1. Количество объектов Book до создания: " << Book::getTotalCount() << endl;
    cout << "Количество книг в библиотеках: " << Library::getBooksInLibrariesCount() << endl;

    // 2. Создание библиотеки и книг
    cout << "\n2. Создание объектов:" << endl;
    Library lib("Центральная городская библиотека", "ул. Ленина, 10");

    // Добавляем книги разных типов
    lib.addBook<MainHallBook>("Преступление и наказание", "Роман", "Достоевский", 15, true);
    lib.addBook<ReadingRoomBook>("Война и мир", "Роман-эпопея", "Толстой", 3, "Историческая литература");
    lib.addBook<MainHallBook>("Анна Каренина", "Роман", "Толстой", 22, false);

    // 3. Вывод информации после создания объектов
    cout << "\n3. Количество объектов Book после создания: " << Book::getTotalCount() << endl;
    cout << "Количество книг в библиотеках: " << Library::getBooksInLibrariesCount() << endl;

    // 4. Вывод информации о библиотеке
    lib.displayAll();

    // 5. Удаление книги
    cout << "\n5. Удаление одной книги:" << endl;
    lib.removeBook(1);

    // 6. Вывод информации после удаления
    cout << "\n6. Количество объектов Book после удаления: " << Book::getTotalCount() << endl;
    cout << "Количество книг в библиотеках: " << Library::getBooksInLibrariesCount() << endl;

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}