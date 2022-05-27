import lists as l
import pyttsx3
import sys
import os

class Commands:
    """ Класс с возможными командами бота """

    def detected_command(self, command):
        """ Метод для распознования команды """

        if command in l.commands_hello:
            Jared.say(l.dictionary['привет'])
        elif command in l.commands_stop:
            Jared.say(l.dictionary['стоп'])
            sys.exit()
        elif command in l.commands_open:
            Jared.open()
            Jared.say(l.dictionary['браузер'])
        elif command in l.commands_shutdown:
            Jared.open()
            Jared.shutdown()
            Jared.say(l.dictionary['выключение пк'])
        elif command in l.commands_time:
            Jared.say(l.dictionary['время'])   
        elif command in l.commands_date:
            Jared.say(l.dictionary['дата'])     
        elif command in l.commands_rand:
            Jared.say(l.dictionary['рандом'])
        else:
            Jared.say(l.dictionary['не знаю'])


class Jared:
    """ Класс для управления ботом """

    def __init__(self, name, sex, text_language, sound_language) -> None:
        """ Конструктор """
        self.name = name
        self.sex = sex
        self.speech_language = text_language
        self.recognition_language = sound_language
        # инициализация инструмента синтеза речи
        self.ttsEng = pyttsx3.init()

    def say(self, text):
        """ Метод для воспроизведения звука """
        self.ttsEng.say(str(text))
        self.ttsEng.runAndWait()

    def open(self):
        """ Открытие браузера """
        import webbrowser
        webbrowser.open('https://www.google.ru', new = 2)

    def shutdown(self):
        """ Выключение компьютера """
        os.system('shutdown /s /t 1')

    def setup_assistant_voice(self, assistant):
        """ Установка голоса по умолчанию (индекс может меняться в зависимости от настроек операционной системы) """
        voices = self.ttsEng.getProperty("voices")

        if assistant.speech_language == "en":
            assistant.recognition_language = "en-US"
            if assistant.sex == "female":
                # Microsoft Zira Desktop - English (United States)
                self.ttsEng.setProperty("voice", voices[1].id)
            else:
                # Microsoft David Desktop - English (United States)
                self.ttsEng.setProperty("voice", voices[2].id)
        else:
            assistant.recognition_language = "ru-RU"
            # Microsoft Irina Desktop - Russian
            self.ttsEng.setProperty("voice", voices[0].id)