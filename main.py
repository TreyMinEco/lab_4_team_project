def Open(file_name, mode):
    """Безпечне відкриття текстового файлу."""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except OSError as error:
        print(f"Файл {file_name} не вдалося відкрити: {error}")
        return None
    else:
        print(f"Файл {file_name} було відкрито")
        return file


def create_input_file():
    """Створення та заповнення файлу TF9_1.txt."""
    file_name = "TF9_1.txt"

    file = Open(file_name, "w")

    if file is None:
        return

    # Початкові тестові рядки різної довжини
    lines = [
        "Короткий рядок",
        "Цей рядок довший за двадцять символів",
        "Рівно 20 символів...",
        "Привіт"
    ]

    for line in lines:
        file.write(line + "\n")

    file.close()

    print("Інформацію успішно додано до TF9_1.txt")
    print("Файл TF9_1.txt закрито")


def process_file():
    """Оброблення TF9_1.txt та створення TF9_2.txt."""
    file1_name = "TF9_1.txt"
    file2_name = "TF9_2.txt"

    file_2_r = Open(file1_name, "r")
    file_2_w = Open(file2_name, "w")

    if file_2_r is not None and file_2_w is not None:
        for line in file_2_r.read().splitlines():

            # Доповнення або обрізання рядка до 20 символів
            if len(line) < 20:
                formatted_line = line.ljust(20)
            else:
                formatted_line = line[:20]

            file_2_w.write(formatted_line + "\n")

        file_2_r.close()
        file_2_w.close()

        print("Файли TF9_1.txt та TF9_2.txt закрито")


def create_backup():
    """Створення дубліката TF9_2.txt під назвою TF9_2(reserve).txt."""
    source_name = "TF9_2.txt"
    backup_name = "TF9_2(reserve).txt"

    file_src = Open(source_name, "r")
    file_dst = Open(backup_name, "w")

    if file_src is not None and file_dst is not None:
        file_dst.write(file_src.read())

        file_src.close()
        file_dst.close()

        print(f"Резервну копію успішно створено: {backup_name}")
        print(f"Файли {source_name} та {backup_name} закрито")


def print_result():
    """Виведення вмісту TF9_2.txt у консоль."""
    file_name = "TF9_2.txt"

    print("\nРезультат з файлу TF9_2:")

    file_3_r = Open(file_name, "r")

    if file_3_r is not None:
        for line in file_3_r.read().splitlines():
            print(f"'{line}' (довжина: {len(line)})")

        file_3_r.close()
        print("Файл TF9_2.txt закрито")


if __name__ == "__main__":
    create_input_file()
    process_file()
    create_backup()
    print_result()
