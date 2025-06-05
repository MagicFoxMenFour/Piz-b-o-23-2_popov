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
    // Конструктор
    Book(string t, string g, string a) : title(t), genre(g), author(a) {}

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
    // Конструктор
    Library(string n, string a) : name(n), address(a) {}

    // Метод для добавления книги в библиотеку
    void addBook(const Book& book) {
        books.push_back(book);
    }

    // Метод для вывода информации о библиотеке и всех книгах
    void display() const {
        cout << "Библиотека: " << name << endl;
        cout << "Адрес: " << address << endl;
        cout << "Количество книг: " << books.size() << endl;
        cout << "Список книг:" << endl;
        cout << "-----------------------------" << endl;

        for (const auto& book : books) {
            book.display();
            cout << "-----------------------------" << endl;
        }
    }

    // Методы для получения информации о библиотеке
    string getName() const { return name; }
    string getAddress() const { return address; }
    int getBookCount() const { return books.size(); }
};

int main() {
    setlocale(LC_ALL, "Rus");
    // Создание библиотеки
    Library lib("Центральная городская библиотека", "ул. Ленина, 10");

    // Добавление книг в библиотеку
    lib.addBook(Book("Преступление и наказание", "Роман", "Фёдор Достоевский"));
    lib.addBook(Book("Война и мир", "Роман-эпопея", "Лев Толстой"));
    lib.addBook(Book("Мастер и Маргарита", "Роман", "Михаил Булгаков"));

    // Вывод информации о библиотеке
    lib.display();

    return 0;
}