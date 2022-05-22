import speech_recognition

def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""
        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Проверьте ваш микрофон")
            return

        # использование online-распознавания через Google 
        try:
            print("Начало распознования...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Нет соединения с интернетом")

        return recognized_data

if __name__ == "__main__":
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи 
        voice_input = record_and_recognize_audio()
        print(voice_input)