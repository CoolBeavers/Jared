import sys
import lists as l
from jared import Jared

class Commands:
    """ Класс с возможными командами бота """

    def __init__(self, command) -> None:
        """ Конструктор класса """
        self.command = command

    def detected_command(self):
        """ Метод для распознования команды """

        if self.command in l.commands_hello:
            Jared.say('привет')
        elif self.command in l.commands_stop:
            sys.exit()
            Jared.say('стоп')
        elif self.command in l.commands_open:
            Jared.open()
            Jared.say('браузер')
        elif self.command in l.commands_shutdown:
            Jared.open()
            Jared.shutdown('выключение пк')
        elif self.command in l.commands_time:
            Jared.say('время')    
        elif self.command in l.commands_date:
            Jared.say('дата')        
        elif self.command in l.commands_rand:
            Jared.say('рандом')    