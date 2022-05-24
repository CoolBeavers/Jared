import user

# Списки с ключевыми словами
commands_hello = ['привет', 'ку', 'дарова', 'салам', 'hello', 'здраствуйте']                        # Приветствие
commands_stop = ['стоп', 'выйти', 'выход', 'конец', 'завершить', 'пока', 'досвидания']              # Выход из системы
commands_open = ['открыть браузер', 'браузер', 'интернет', 'гугл', 'яндекс', 'опера']               # Открытие браузера
commands_shutdown = ['выключи компьютер', 'выключить компьютер', 'выключить пк', 'выключи пк']      # Выключение компьютера
commands_time = ['время', 'сколько времени', 'какое время', 'time', 'сколько часов']                # Предствление времени
commands_date = ['дата', 'какая дата', 'какое число', 'сегодня', 'месяц', 'год']                    # Предствление даты
commands_rand = ['рандом', 'случайное число', 'рандомное число']                                    # Случайное число

# Словарь для воспроизведения речи ботом
dictionary = {
    'стоп' : 'Досвидания, ' + user.name,
    'привет' : 'Добрый день, ' + user.name,
    'браузер' : 'Уже открываю!',
    'выключение пк' : 'Выключаю!',
    'время' : 'Сейчас ' + user.hour + user.minute,
    'дата' : 'Сегодня ' + user.day + user.month + user.year + ' года',
    'рандом' : 'Я загадал число ' + user.rand
}


# Сделать подбрасывание монеты: орёл или решка
# Открытие ВК, Ютуб, Дискорд
# Научить гуглить что либо (Чтоб в адресную строку браузера сразу поступал запрос с текстом)
# Проверка почты на наличие писем