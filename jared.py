import user

class Jared:
    """ Класс для управления ботом """

    dictionary = {
        'стоп' : 'Досвидания, ' + user.name,
        'привет' : 'Здраствуйте, ' + user.name,
        'браузер' : 'Уже открываю!',
        'выключение пк' : 'Выключаю!',
    }

    def __init__(self) -> None:
        """ Конструктор """
        pass

    def say(self, text):
        """ Метод для воспроизведения звука """
        pass

    def open(self):
        """ Открытие браузера """
        import webbrowser
        webbrowser.open('https://www.google.ru', new=2)

    def shutdown(self):
        """ Выключение компьютера """
        import os
        os.system('shutdown /s /t 1')