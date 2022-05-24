import lists as l

class Jared:
    """ Класс для управления ботом """

    def __init__(self) -> None:
        """ Конструктор """
        pass

    def say(self, text):
        """ Метод для воспроизведения звука """
        # В файле lists.py есть словарь по которому нужно делать поиск text (параметр функции)
        # Если ничего не найдено, то бот должен говорить "Извините, такому я ещё не обучился"
        pass

    def open(self):
        """ Открытие браузера """
        import webbrowser
        webbrowser.open('https://www.google.ru', new = 2)

    def shutdown(self):
        """ Выключение компьютера """
        import os
        os.system('shutdown /s /t 1')