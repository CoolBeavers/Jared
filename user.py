import os
import datetime 
import random

name = os.getlogin()                # Имя пользователя (Windows аккаунт)

now = datetime.datetime.now()       # Текущая дата и время
hour = now.hour
minute = now.minute
day = now.day
month = now.strftime("%B")          # Получение название месяца из даты
year = now.year

rand = random.randint(0, 100)