def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        print("Действие с фильмами:")
        print("1 - Добавление фильма\n"
              "2 - Каталог фильмов\n"
              "3 - Просмотр определенного фильма\n"
              "4 - Удаление фильма\n"
              "q - Выход из программы\n")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добавление фильма")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "режиссера":  None,
            "длительность": None,
            "студию": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} фильма: ")
        return dict_article

    @add_title("Список фильмов")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")

    @add_title("Ввод названия фильма")
    def get_user_article(self):
        user_article = input("Введите название фильма: ")
        return user_article

    @add_title("Просмотр фильма")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} фильма = {article[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма")
    def remove_single_article(self, article):
        print(f"Фильм {article} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")