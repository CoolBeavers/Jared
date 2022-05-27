import sys
import lists as l
from jared import Jared



#           Не используюется, перемещён в класс Jared




class Commands:
    """ Класс с возможными командами бота """

    def __init__(self) -> None:
        """ Конструктор класса """
        pass

    def detected_command(self, command):
        """ Метод для распознования команды """

        if command in l.commands_hello:
            Jared.say('привет')
        elif command in l.commands_stop:
            sys.exit()
            Jared.say('стоп')
        elif command in l.commands_open:
            Jared.open()
            Jared.say('браузер')
        elif command in l.commands_shutdown:
            Jared.open()
            Jared.shutdown('выключение пк')
        elif command in l.commands_time:
            Jared.say('время')    
        elif command in l.commands_date:
            Jared.say('дата')        
        elif command in l.commands_rand:
            Jared.say('рандом')    