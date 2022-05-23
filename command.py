import sys
from jared import Jared

# Списки с ключевыми словами
# Лучше перенести этот список в отдельный файл
list_commands_hello = ['привет', 'ку', 'дарова', 'салам', 'hello', 'здраствуйте']                        # Приветствие
list_commands_stop = ['стоп', 'выйти', 'выход', 'конец', 'завершить', 'пока', 'досвидания']              # Выход из системы
list_commands_open = ['открыть браузер', 'браузер', 'интернет', 'гугл', 'яндекс', 'опера']               # Открытие браузера
list_commands_shutdown = ['выключи компьютер', 'выключить компьютер', 'выключить пк', 'выключи пк']      # Выключение компьютера
list_commands_time = ['время', 'сколько времени', 'какое время', 'time', 'сколько часов']                # Предствление времени
list_commands_date = ['дата', 'какая дата', 'какое число', 'сегодня', 'месяц', 'год']                    # Предствление даты
list_commands_rand = ['рандом', 'случайное число', 'рандомное число']                                    # Случайное число

class Commands:
    """ Класс с возможными командами бота """

    def __init__(self, command) -> None:
        """ Конструктор класса """
        self.command = command

    def detected_command(self):
        """ Метод для распознования команды """

        if self.command in list_commands_hello:
            Jared.say('привет')
        elif self.command in list_commands_stop:
            sys.exit()
            Jared.say('стоп')
        elif self.command in list_commands_open:
            Jared.open()
            Jared.say('браузер')
        elif self.command in list_commands_shutdown:
            Jared.open()
            Jared.shutdown('выключение пк')