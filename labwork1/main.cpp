#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

// Структура для хранения статистики по файлу
struct FileStats {
    std::string filename;  
    size_t lines = 0;      
    size_t words = 0;      
    size_t bytes = 0;      
    size_t chars = 0;      
};

// Структура для хранения настроек программы 
struct ProgramOptions {
    bool show_lines = false;
    bool show_words = false;
    bool show_bytes = false; 
    bool show_chars = false;
    bool default_options = true;
};

// Функция проверки существования файла
bool file_exists(const std::string& filename) {
    std::ifstream file(filename);
    return file.good();  // Если файл успешно открыт, возвращает true
}

// Функция подсчета статистики для файла
FileStats count_stats(const std::string& filename) {
    FileStats stats;
    stats.filename = filename;

    // Открываем файл в бинарном режиме
    std::ifstream file(filename, std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "WordCount: " << filename << ": No such file or directory\n";
        return stats;
    }

    char ch;          
    bool in_word = false;

    // Определяем размер файла в байтах
    file.seekg(0, std::ios::end);
    stats.bytes = file.tellg();
    file.seekg(0, std::ios::beg);

    // Читаем файл посимвольно
    while (file.get(ch)) {
        stats.chars++;  // Увеличиваем счетчик символов

        // Если символ - перевод строки, увеличиваем счетчик строк
        if (ch == '\n') {
            stats.lines++;
        }

        // Если символ - пробельный, и мы были внутри слова,
        // увеличиваем счетчик слов
        if (std::isspace(static_cast<unsigned char>(ch))) {
            if (in_word) {
                stats.words++;
                in_word = false;
            }
        }
        else {
            in_word = true;  
        }
    }

    // Если файл заканчивается словом 
    if (in_word) {
        stats.words++;
    }

    return stats;
}

// Функция вывода статистики в соответствии с настройками
void print_stats(const FileStats& stats, const ProgramOptions& options) {
    // Если используются настройки по умолчанию
    if (options.default_options) {
        std::cout << stats.lines << " " << stats.words << " " << stats.bytes << " " << stats.filename << "\n";
        return;
    }

    bool first = true;  // Флаг для управления пробелами между значениями

    // Выводим запрошенные значения в указанном порядке
    if (options.show_lines) {
        if (!first) std::cout << " ";
        std::cout << stats.lines;
        first = false;
    }

    if (options.show_words) {
        if (!first) std::cout << " ";
        std::cout << stats.words;
        first = false;
    }

    if (options.show_bytes) {
        if (!first) std::cout << " ";
        std::cout << stats.bytes;
        first = false;
    }

    if (options.show_chars) {
        if (!first) std::cout << " ";
        std::cout << stats.chars;
        first = false;
    }

    // Если что-то было выведено, добавляем имя файла
    if (!first) {
        std::cout << " " << stats.filename;
    }

    std::cout << "\n";
}

// Функция разбора аргументов командной строки
void parse_args(int argc, char** argv, ProgramOptions& options, std::vector<std::string>& filenames) {
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];

        // Обработка опций (начинаются с '-')
        if (arg[0] == '-') {
            options.default_options = false;  // Используются нестандартные опции

            // Обработка длинных опций (--lines, --words и т.д.)
            if (arg == "--lines") {
                options.show_lines = true;
            }
            else if (arg == "--words") {
                options.show_words = true;
            }
            else if (arg == "--bytes") {
                options.show_bytes = true;
            }
            else if (arg == "--chars") {
                options.show_chars = true;
            }
            // Обработка коротких опций (-l, -w, -c, -m и их комбинаций)
            else if (arg.size() > 1 && arg[1] != '-') {
                for (size_t j = 1; j < arg.size(); ++j) {
                    switch (arg[j]) {
                    case 'l': options.show_lines = true; break;
                    case 'w': options.show_words = true; break;
                    case 'c': options.show_bytes = true; break;
                    case 'm': options.show_chars = true; break;
                    default:
                        // Неизвестная опция
                        std::cerr << "WordCount: invalid option -- '" << arg[j] << "'\n";
                        exit(EXIT_FAILURE);
                    }
                }
            }
            else {
                // Неизвестная опция
                std::cerr << "WordCount: unrecognized option '" << arg << "'\n";
                exit(EXIT_FAILURE);
            }
        }
        else {
            // Аргумент не является опцией - добавляем в список файлов
            filenames.push_back(arg);
        }
    }

    // Если используются опции по умолчанию, показываем строки, слова и байты
    if (options.default_options) {
        options.show_lines = true;
        options.show_words = true;
        options.show_bytes = true;
    }
}

int main(int argc, char** argv) {
    // Проверка на минимальное количество аргументов
    if (argc < 2) {
        std::cerr << "Usage: WordCount [OPTION]... [FILE]...\n";
        return EXIT_FAILURE;
    }

    ProgramOptions options;  // Настройки программы
    std::vector<std::string> filenames;  // Список файлов для обработки

    // Разбираем аргументы командной строки
    parse_args(argc, argv, options, filenames);

    // Проверка, что указаны файлы для обработки
    if (filenames.empty()) {
        std::cerr << "WordCount: no files specified\n";
        return EXIT_FAILURE;
    }

    // Обрабатываем каждый файл
    for (const auto& filename : filenames) {
        if (!file_exists(filename)) {
            std::cerr << "WordCount: " << filename << ": No such file or directory\n";
            continue;
        }

        // Получаем статистику и выводим её
        FileStats stats = count_stats(filename);
        print_stats(stats, options);
    }

    return EXIT_SUCCESS;
}