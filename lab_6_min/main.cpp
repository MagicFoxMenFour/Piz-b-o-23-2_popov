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
    static int totalCount;

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

    virtual void displayFullInfo() const = 0;
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
        cout << "Автор: " << getAuthor() << endl;
        cout << "Жанр: " << getGenre() << endl;
        cout << "Номер полки: " << shelfNumber << endl;
        cout << "Доступна для выноса: " << (availableForLoan ? "Да" : "Нет") << endl;
    }
};

// Класс Библиотека с перегруженными операторами
class Library {
private:
    string name;
    string address;
    vector<unique_ptr<Book>> books;
    static int booksInLibrariesCount;

public:
    Library(string n, string a) : name(n), address(a) {
        cout << "Вызван конструктор класса Library: " << name << endl;
    }

    // Удаляем конструктор копирования и оператор присваивания
    Library(const Library&) = delete;
    Library& operator=(const Library&) = delete;

    // Конструктор перемещения
    Library(Library&& other) noexcept
        : name(move(other.name)), address(move(other.address)), books(move(other.books)) {
        cout << "Вызван конструктор перемещения класса Library" << endl;
    }

    // Оператор перемещения
    Library& operator=(Library&& other) noexcept {
        name = move(other.name);
        address = move(other.address);
        books = move(other.books);
        cout << "Вызван оператор перемещения класса Library" << endl;
        return *this;
    }

    ~Library() {
        cout << "Вызван деструктор класса Library: " << name << endl;
    }

    // Оператор + для добавления книги (принимает rvalue ссылку)
    Library& operator+(unique_ptr<MainHallBook>&& book) {
        books.push_back(move(book));
        booksInLibrariesCount++;
        cout << "Добавлена книга через оператор +: " << books.back()->getTitle() << endl;
        return *this;
    }

    // Префиксный оператор ++
    Library& operator++() {
        books.emplace_back(make_unique<MainHallBook>());
        booksInLibrariesCount++;
        cout << "Добавлена книга по умолчанию через префиксный ++" << endl;
        return *this;
    }

    // Постфиксный оператор ++
    Library operator++(int) {
        Library temp(move(*this));
        books.emplace_back(make_unique<MainHallBook>());
        booksInLibrariesCount++;
        cout << "Добавлена книга по умолчанию через постфиксный ++" << endl;
        return temp;
    }

    // Оператор [] для доступа к элементам
    Book& operator[](size_t index) {
        if (index >= books.size()) {
            throw out_of_range("Индекс выходит за границы массива");
        }
        return *books[index];
    }

    // Дружественная функция для оператора вывода
    friend ostream& operator<<(ostream& os, const Library& lib);

    static int getBooksInLibrariesCount() { return booksInLibrariesCount; }
};

int Library::booksInLibrariesCount = 0;

// Глобальный оператор << для вывода библиотеки
ostream& operator<<(ostream& os, const Library& lib) {
    os << "\n=== Информация о библиотеке ===" << endl;
    os << "Название: " << lib.name << endl;
    os << "Адрес: " << lib.address << endl;
    os << "Количество книг: " << lib.books.size() << endl;

    if (!lib.books.empty()) {
        os << "\n=== Список книг ===" << endl;
        for (const auto& book : lib.books) {
            book->displayFullInfo();
            os << "-------------------" << endl;
        }
    }
    return os;
}

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 6: ПЕРЕГРУЗКА ОПЕРАТОРОВ ===" << endl;

    // Создание библиотеки
    Library lib("Центральная городская библиотека", "ул. Ленина, 10");

    // Демонстрация оператора +
    lib + make_unique<MainHallBook>("Преступление и наказание", "Роман", "Достоевский", 15, true);
    lib + make_unique<MainHallBook>("Война и мир", "Роман-эпопея", "Толстой", 22, false);

    // Демонстрация префиксного и постфиксного ++
    ++lib;
    lib++;

    // Демонстрация оператора []
    try {
        cout << "\nДоступ к книге по индексу 1:" << endl;
        lib[1].displayFullInfo();
    }
    catch (const out_of_range& e) {
        cerr << "Ошибка: " << e.what() << endl;
    }

    // Демонстрация оператора <<
    cout << lib;

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}