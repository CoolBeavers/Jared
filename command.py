import sys

list_commands_stop = ['стоп', 'выйти', 'выход']

class Commands:
    def __init__(self, command) -> None:
        self.command = command

    def detected_command(self):
        if self.command in list_commands_stop:
            sys.exit()