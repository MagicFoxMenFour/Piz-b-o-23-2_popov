#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <stdexcept>

using namespace std;

// Пользовательские классы исключений
class BookException : public std::runtime_error {
public:
    BookException(const string& msg) : runtime_error(msg) {}
};

class InvalidBookOperation : public BookException {
public:
    InvalidBookOperation(const string& msg) : BookException(msg) {}
};

class LibraryOperationException : public BookException {
public:
    LibraryOperationException(const string& msg) : BookException(msg) {}
};

// Базовый абстрактный класс Книга
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
        if (t.empty() || g.empty() || a.empty()) {
            throw invalid_argument("Название, жанр и автор не могут быть пустыми");
        }
        totalCount++;
    }

    virtual ~Book() {
        totalCount--;
    }

    virtual void displayFullInfo() const = 0;

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
        if (sn < 0) {
            throw InvalidBookOperation("Номер полки не может быть отрицательным");
        }
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

// Класс Библиотека
class Library {
private:
    string name;
    string address;
    vector<unique_ptr<Book>> books;

public:
    Library(string n, string a) : name(n), address(a) {
        if (n.empty() || a.empty()) {
            throw invalid_argument("Название и адрес библиотеки не могут быть пустыми");
        }
    }

    void addBook(unique_ptr<Book> book) {
        if (!book) {
            throw LibraryOperationException("Попытка добавить пустую книгу");
        }
        books.push_back(move(book));
    }

    Book& getBook(size_t index) {
        if (index >= books.size()) {
            throw out_of_range("Индекс книги выходит за границы");
        }
        return *books[index];
    }

    void displayAll() const {
        if (books.empty()) {
            throw LibraryOperationException("В библиотеке нет книг");
        }
        for (const auto& book : books) {
            book->displayFullInfo();
            cout << "-------------------" << endl;
        }
    }
};

// Функция, которая может генерировать разные исключения
void processLibrary(int choice) {
    Library lib("Центральная библиотека", "ул. Ленина, 10");

    try {
        if (choice == 1) {
            throw 42; // Генерируем исключение типа int
        }
        else if (choice == 2) {
            throw string("Ошибка обработки библиотеки"); // Генерируем исключение типа string
        }
        else if (choice == 3) {
            lib.addBook(nullptr); // Вызовет LibraryOperationException
        }
        else if (choice == 4) {
            auto book = make_unique<MainHallBook>("", "Роман", "Достоевский", 1, true); // Вызовет invalid_argument
            lib.addBook(move(book));
        }
        else {
            lib.getBook(10); // Вызовет out_of_range
        }
    }
    catch (const invalid_argument& e) {
        cout << "Локальная обработка invalid_argument: " << e.what() << endl;
        throw; // Перебрасываем исключение наверх
    }
    catch (const out_of_range& e) {
        cout << "Локальная обработка out_of_range: " << e.what() << endl;
        throw LibraryOperationException("Ошибка доступа к книге");
    }
}

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 8: ОБРАБОТКА ИСКЛЮЧЕНИЙ ===" << endl;

    // Демонстрация обработки исключений
    for (int i = 1; i <= 5; i++) {
        cout << "\nТест #" << i << ":" << endl;

        try {
            processLibrary(i);
        }
        catch (int e) {
            cout << "Поймано исключение типа int: " << e << endl;
        }
        catch (const string& e) {
            cout << "Поймано исключение типа string: " << e << endl;
        }
        catch (const InvalidBookOperation& e) {
            cout << "Поймано пользовательское исключение InvalidBookOperation: " << e.what() << endl;
        }
        catch (const LibraryOperationException& e) {
            cout << "Поймано пользовательское исключение LibraryOperationException: " << e.what() << endl;
        }
        catch (const exception& e) {
            cout << "Поймано стандартное исключение: " << e.what() << endl;
        }
        catch (...) {
            cout << "Поймано неизвестное исключение" << endl;
        }
    }

    // Демонстрация локальной обработки без передачи наверх
    cout << "\nДемонстрация локальной обработки:" << endl;
    try {
        Library lib("", "ул. Ленина, 10"); // Вызовет invalid_argument
    }
    catch (const invalid_argument& e) {
        cout << "Ошибка создания библиотеки обработана локально: " << e.what() << endl;
    }

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}