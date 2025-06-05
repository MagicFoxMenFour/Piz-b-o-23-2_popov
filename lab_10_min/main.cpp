#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <memory>
#include <algorithm>

using namespace std;

// Базовый класс Книга
class Book {
protected:
    string title;
    string genre;
    string author;

public:
    Book() : title("Неизвестно"), genre("Неизвестно"), author("Неизвестно") {}
    Book(string t, string g, string a) : title(t), genre(g), author(a) {}
    virtual ~Book() {}

    virtual void display() const {
        cout << "Название: " << title << endl;
        cout << "Автор: " << author << endl;
        cout << "Жанр: " << genre << endl;
    }

    string getTitle() const { return title; }
    void setTitle(const string& t) { title = t; }
};

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
    ReadingRoomBook() : Book(), roomNumber(0), readingTheme("Неизвестно") {}
    ReadingRoomBook(string t, string g, string a, int rn, string rt)
        : Book(t, g, a), roomNumber(rn), readingTheme(rt) {
    }

    void display() const override {
        Book::display();
        cout << "Номер читального зала: " << roomNumber << endl;
        cout << "Тематика: " << readingTheme << endl;
    }
};

int main() {
    setlocale(LC_ALL, "Rus");
    cout << "=== РАБОТА С КОНТЕЙНЕРАМИ STL ===" << endl;

    // 1. Создание и заполнение контейнера vector встроенным типом (int)
    vector<int> numbers = { 10, 20, 30, 40, 50 };
    cout << "\n1. Вектор чисел (int):" << endl;
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;

    // 2. Изменение контейнера vector
    numbers.erase(remove(numbers.begin(), numbers.end(), 30), numbers.end());
    numbers[1] = 25;
    numbers.push_back(60);

    cout << "\n2. Измененный вектор чисел:" << endl;
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // 3. Создание и заполнение контейнера list пользовательским типом (Book)
    list<unique_ptr<Book>> library;
    library.push_back(make_unique<Book>("1984", "Антиутопия", "Оруэлл"));
    library.push_back(make_unique<MainHallBook>("Преступление и наказание", "Роман", "Достоевский", 15, true));
    library.push_back(make_unique<ReadingRoomBook>("Война и мир", "Роман-эпопея", "Толстой", 3, "История"));

    cout << "\n3. Список книг в библиотеке:" << endl;
    for (const auto& book : library) {
        book->display();
        cout << "-------------------" << endl;
    }

    // 4. Изменение контейнера list
    // Удаляем книгу с определенным названием
    library.remove_if([](const unique_ptr<Book>& b) {
        return b->getTitle() == "1984";
        });

    // Изменяем первую книгу
    if (!library.empty()) {
        library.front()->setTitle("Новое название книги");
    }

    // Добавляем новую книгу
    library.push_back(make_unique<MainHallBook>("Анна Каренина", "Роман", "Толстой", 22, false));

    cout << "\n4. Измененный список книг (с итераторами):" << endl;
    for (auto it = library.begin(); it != library.end(); ++it) {
        (*it)->display();
        cout << "-------------------" << endl;
    }

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}