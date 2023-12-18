try:
    with open("TF12_1.txt", "w") as file1:
        file1.write("abcdefghij\n")
        file1.write("klmnopqrst\n")
        file1.write("uvwxyz\n")

    with open("TF12_1.txt", "r") as file1, open("TF12_2.txt", "w") as file2:
        content = file1.read().replace("\n", "")
        for i in range(1, len(content) + 1):
            file2.write(content[:i] + "\n")

    with open("TF12_2.txt", "r") as file2:
        print("Вміст файла TF12_2:")
        for line in file2:
            print(line.strip())

except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except Exception as e:
    print(f"Виникла помилка: {e}")
