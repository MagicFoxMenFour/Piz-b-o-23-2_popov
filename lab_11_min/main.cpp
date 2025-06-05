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
    string getAuthor() const { return author; }
    string getGenre() const { return genre; }

    // Оператор для сравнения книг по названию (для сортировки)
    bool operator<(const Book& other) const {
        return title < other.title;
    }
    bool operator>(const Book& other) const {
        return title > other.title;
    }
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
    cout << "=== РАБОТА С КОНТЕЙНЕРАМИ И АЛГОРИТМАМИ STL ===" << endl;

    // 1. Создание и заполнение контейнера vector книгами
    vector<unique_ptr<Book>> library;
    library.push_back(make_unique<Book>("1984", "Антиутопия", "Оруэлл"));
    library.push_back(make_unique<MainHallBook>("Преступление и наказание", "Роман", "Достоевский", 15, true));
    library.push_back(make_unique<ReadingRoomBook>("Война и мир", "Роман-эпопея", "Толстой", 3, "История"));
    library.push_back(make_unique<Book>("Мастер и Маргарита", "Роман", "Булгаков"));
    library.push_back(make_unique<MainHallBook>("Анна Каренина", "Роман", "Толстой", 22, false));

    // 2. Сортировка по убыванию (по названию)
    sort(library.begin(), library.end(),
        [](const unique_ptr<Book>& a, const unique_ptr<Book>& b) {
            return *a > *b;
        });

    cout << "\n1. Контейнер после сортировки по убыванию:" << endl;
    for (const auto& book : library) {
        book->display();
        cout << "-------------------" << endl;
    }

    // 3. Поиск книги с названием "Война и мир"
    auto it = find_if(library.begin(), library.end(),
        [](const unique_ptr<Book>& b) {
            return b->getTitle() == "Война и мир";
        });

    if (it != library.end()) {
        cout << "\n2. Найдена книга:" << endl;
        (*it)->display();
    }
    else {
        cout << "\n2. Книга не найдена" << endl;
    }

    // 4. Перемещение книг Достоевского в другой контейнер (list)
    list<unique_ptr<Book>> dostoevskyBooks;
    auto new_end = remove_if(library.begin(), library.end(),
        [&dostoevskyBooks](unique_ptr<Book>& b) {
            if (b->getAuthor() == "Достоевский") {
                dostoevskyBooks.push_back(move(b));
                return true;
            }
            return false;
        });
    library.erase(new_end, library.end());

    cout << "\n3. Основной контейнер после перемещения книг Достоевского:" << endl;
    for (const auto& book : library) {
        book->display();
        cout << "-------------------" << endl;
    }

    cout << "\n4. Контейнер с книгами Достоевского:" << endl;
    for (const auto& book : dostoevskyBooks) {
        book->display();
        cout << "-------------------" << endl;
    }

    // 5. Сортировка обоих контейнеров по возрастанию
    sort(library.begin(), library.end(),
        [](const unique_ptr<Book>& a, const unique_ptr<Book>& b) {
            return *a < *b;
        });

    dostoevskyBooks.sort(
        [](const unique_ptr<Book>& a, const unique_ptr<Book>& b) {
            return *a < *b;
        });

    cout << "\n5. Основной контейнер после сортировки по возрастанию:" << endl;
    for (const auto& book : library) {
        book->display();
        cout << "-------------------" << endl;
    }

    cout << "\n6. Контейнер Достоевского после сортировки по возрастанию:" << endl;
    for (const auto& book : dostoevskyBooks) {
        book->display();
        cout << "-------------------" << endl;
    }

    cout << "\n=== ЗАВЕРШЕНИЕ ПРОГРАММЫ ===" << endl;
    return 0;
}