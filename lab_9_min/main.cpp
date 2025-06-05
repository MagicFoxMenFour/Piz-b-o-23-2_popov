#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <stdexcept>
#include <fstream>

using namespace std;

// Пользовательские классы исключений
class BookException : public std::runtime_error {
public:
    BookException(const string& msg) : runtime_error(msg) {}
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
    virtual void saveToStream(ostream& os) const = 0;
    virtual void loadFromStream(istream& is) = 0;

    static int getTotalCount() { return totalCount; }
    string getTitle() const { return title; }
    string getAuthor() const { return author; }
    string getGenre() const { return genre; }

    friend ostream& operator<<(ostream& os, const Book& book);
    friend istream& operator>>(istream& is, Book& book);
};

int Book::totalCount = 0;

// Глобальные операторы ввода/вывода для базового класса
ostream& operator<<(ostream& os, const Book& book) {
    book.saveToStream(os);
    return os;
}

istream& operator>>(istream& is, Book& book) {
    book.loadFromStream(is);
    return is;
}

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
            throw BookException("Номер полки не может быть отрицательным");
        }
    }

    void displayFullInfo() const override {
        cout << "=== Книга основного зала ===" << endl;
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
        cout << "Номер полки: " << shelfNumber << endl;
        cout << "Доступна для выноса: " << (availableForLoan ? "Да" : "Нет") << endl;
    }

    void saveToStream(ostream& os) const override {
        os << "MainHallBook" << endl;
        os << title << endl;
        os << genre << endl;
        os << author << endl;
        os << shelfNumber << endl;
        os << availableForLoan << endl;
    }

    void loadFromStream(istream& is) override {
        getline(is, title);
        getline(is, genre);
        getline(is, author);
        is >> shelfNumber;
        is >> availableForLoan;
        is.ignore(); // Пропустить символ новой строки
    }
};

// Класс Библиотека
class Library {
private:
    string name;
    string address;
    vector<unique_ptr<Book>> books;

public:
    Library() = default;

    Library(string n, string a) : name(n), address(a) {
        if (n.empty() || a.empty()) {
            throw invalid_argument("Название и адрес библиотеки не могут быть пустыми");
        }
    }

    void addBook(unique_ptr<Book> book) {
        if (!book) {
            throw BookException("Попытка добавить пустую книгу");
        }
        books.push_back(move(book));
    }

    void saveToFile(const string& filename) const {
        ofstream outFile(filename);
        if (!outFile) {
            throw BookException("Не удалось открыть файл для записи");
        }

        outFile << name << endl;
        outFile << address << endl;
        outFile << books.size() << endl;

        for (const auto& book : books) {
            outFile << *book;
        }
    }

    void loadFromFile(const string& filename) {
        ifstream inFile(filename);
        if (!inFile) {
            throw BookException("Не удалось открыть файл для чтения");
        }

        books.clear();
        getline(inFile, name);
        getline(inFile, address);

        int bookCount;
        inFile >> bookCount;
        inFile.ignore(); // Пропустить символ новой строки

        for (int i = 0; i < bookCount; ++i) {
            string bookType;
            getline(inFile, bookType);

            unique_ptr<Book> book;
            if (bookType == "MainHallBook") {
                book = make_unique<MainHallBook>();
                inFile >> *book;
            }
            // Добавьте другие типы книг при необходимости

            if (book) {
                books.push_back(move(book));
            }
        }
    }

    void displayAll() const {
        if (books.empty()) {
            throw BookException("В библиотеке нет книг");
        }
        cout << "Библиотека: " << name << endl;
        cout << "Адрес: " << address << endl;
        cout << "Количество книг: " << books.size() << endl;

        for (const auto& book : books) {
            book->displayFullInfo();
            cout << "-------------------" << endl;
        }
    }
};

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== ЛАБОРАТОРНАЯ РАБОТА 9: ВВОД/ВЫВОД И РАБОТА С ФАЙЛАМИ ===" << endl;

    try {
        // Создаем библиотеку и добавляем книги
        Library lib("Центральная библиотека", "ул. Ленина, 10");
        lib.addBook(make_unique<MainHallBook>("Преступление и наказание", "Роман", "Достоевский", 15, true));
        lib.addBook(make_unique<MainHallBook>("Война и мир", "Роман-эпопея", "Толстой", 22, false));

        // Демонстрация оператора << для книги
        MainHallBook book;
        cout << "\nВведите данные о книге (название, жанр, автор, номер полки, доступность):" << endl;
        cin >> book;
        cout << "\nВы ввели книгу:\n" << book << endl;

        // Сохраняем библиотеку в файл
        const string filename = "library.txt";
        lib.saveToFile(filename);
        cout << "\nБиблиотека сохранена в файл: " << filename << endl;

        // Загружаем библиотеку из файла
        Library loadedLib;
        loadedLib.loadFromFile(filename);
        cout << "\nБиблиотека загружена из файла:" << endl;
        loadedLib.displayAll();

    }
    catch (const exception& e) {
        cerr << "Ошибка: " << e.what() << endl;
        return 1;
    }

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}