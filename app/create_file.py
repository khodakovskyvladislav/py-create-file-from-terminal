
import sys
import os
from datetime import datetime


def create_file() -> None:
    arguments = sys.argv[1:]

    directories = []
    filename = None
    mode = None

    # 1. Розбираємо аргументи термінала
    for argument in arguments:
        if argument == "-d":
            mode = "directory"

        elif argument == "-f":
            mode = "file"

        elif mode == "directory":
            directories.append(argument)

        elif mode == "file":
            if filename is not None:
                raise ValueError("Only one filename is allowed")
            filename = argument

    # 2. Створюємо директорії, якщо вони вказані
    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    # 3. Якщо назви файлу немає, завершуємо роботу
    if filename is None:
        return

    # 4. Формуємо повний шлях до файлу
    file_path = os.path.join(directory_path, filename)

    # 5. Отримуємо поточну дату й час
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )   

    # 6. Відкриваємо файл для дописування
    with open(file_path, "a", encoding="utf-8") as file:
        if file_has_content:
            file.write("\n")

        file.write(f"{timestamp}\n")

        line_number = 1

        # 7. Читаємо текст, поки не введуть stop
        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{line_number} {content}\n")
            line_number += 1


create_file()
