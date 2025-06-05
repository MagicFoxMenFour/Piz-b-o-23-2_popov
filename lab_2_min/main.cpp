#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Класс Книга
class Book {
private:
    string title;
    string genre;
    string author;

public:
    // Конструктор без параметров
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {
        cout << "Вызван конструктор без параметров класса Book" << endl;
    }

    // Конструктор с параметрами
    Book(string t, string g, string a) : title(t), genre(g), author(a) {
        cout << "Вызван конструктор с параметрами класса Book: " << title << endl;
    }

    // Конструктор копирования
    Book(const Book& other) : title(other.title), genre(other.genre), author(other.author) {
        cout << "Вызван конструктор копирования класса Book: " << title << " (копия)" << endl;
    }

    // Деструктор
    ~Book() {
        cout << "Вызван деструктор класса Book: " << title << endl;
    }

    // Методы для получения информации о книге
    string getTitle() const { return title; }
    string getGenre() const { return genre; }
    string getAuthor() const { return author; }

    // Метод для вывода информации о книге
    void display() const {
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
    }
};

// Класс Библиотека
class Library {
private:
    string name;
    string address;
    vector<Book> books;

public:
    // Конструктор без параметров
    Library() : name("Неизвестно"), address("Неизвестно") {
        cout << "Вызван конструктор без параметров класса Library" << endl;
    }

    // Конструктор с параметрами
    Library(string n, string a) : name(n), address(a) {
        cout << "Вызван конструктор с параметрами класса Library: " << name << endl;
    }

    // Конструктор копирования
    Library(const Library& other) : name(other.name + " (копия)"), address(other.address), books(other.books) {
        cout << "Вызван конструктор копирования класса Library: " << name << endl;
    }

    // Деструктор
    ~Library() {
        cout << "Вызван деструктор класса Library: " << name << endl;
    }

    // Метод для добавления книги в библиотеку (создает книгу с параметрами)
    void addBookWithParams(string title, string genre, string author) {
        Book newBook(title, genre, author); // Создание через конструктор с параметрами
        books.push_back(newBook);
        cout << "Книга добавлена через метод с параметрами: " << title << endl;
    }

    // Метод для создания копий книги
    void addCopiesOfBook(const Book& book, int count) {
        for (int i = 0; i < count; ++i) {
            books.push_back(Book(book)); // Используем конструктор копирования
        }
        cout << "Добавлено " << count << " копий книги: " << book.getTitle() << endl;
    }

    // Метод для вывода информации о библиотеке и всех книгах
    void display() const {
        cout << "\nИнформация о библиотеке:" << endl;
        cout << "Библиотека: " << name << endl;
        cout << "Адрес: " << address << endl;
        cout << "Количество книг: " << books.size() << endl;

        if (!books.empty()) {
            cout << "\nСписок книг:" << endl;
            cout << "-----------------------------" << endl;

            for (const auto& book : books) {
                book.display();
                cout << "-----------------------------" << endl;
            }
        }
    }

    // Методы для получения информации о библиотеке
    string getName() const { return name; }
    string getAddress() const { return address; }
    int getBookCount() const { return books.size(); }
};

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== Демонстрация работы конструкторов и деструкторов ===" << endl;

    // 1. Создание библиотеки через конструктор с параметрами
    cout << "\n1. Создание библиотеки:" << endl;
    Library lib("Центральная городская библиотека", "ул. Ленина, 10");

    // 2. Создание книги через конструктор с параметрами и добавление в библиотеку
    cout << "\n2. Создание и добавление книги:" << endl;
    Book book1("Преступление и наказание", "Роман", "Фёдор Достоевский");
    lib.addCopiesOfBook(book1, 1); // Добавляем 1 копию

    // 3. Добавление книги через метод с параметрами
    cout << "\n3. Добавление книги через метод с параметрами:" << endl;
    lib.addBookWithParams("Война и мир", "Роман-эпопея", "Лев Толстой");

    // 4. Создание копий книги
    cout << "\n4. Создание копий книги:" << endl;
    Book book2("Мастер и Маргарита", "Роман", "Михаил Булгаков");
    lib.addCopiesOfBook(book2, 2); // Добавляем 2 копии

    // 5. Создание библиотеки через конструктор без параметров
    cout << "\n5. Создание библиотеки через конструктор без параметров:" << endl;
    Library lib2;
    lib2.display();

    // 6. Создание копии библиотеки
    cout << "\n6. Создание копии библиотеки:" << endl;
    Library libCopy(lib);
    libCopy.display();

    cout << "\n=== Завершение программы, вызов деструкторов ===" << endl;
    return 0;
}