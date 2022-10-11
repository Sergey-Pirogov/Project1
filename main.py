import time                             # Загружаем возможность работы с временем

def hello():                            # Приветствие
    print("-----------------------")
    time.sleep(0.8)
    print("Добро пожаловать в игру")
    time.sleep(0.8)
    print("Крестики-Нолики!")
    time.sleep(0.8)
    print("-----------------------")
    print()
    return

hello()
def rules():                            # Правила
    print("-----------------------------")
    print("Правила игры Крестики-Нолики:")
    print("-----------------------------")
    print()
    time.sleep(1.5)
    print("Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).")
    time.sleep(4)
    print()
    print("Первый, выстроивший в ряд 3 своих фигуры по вертикали,горизонтали или диагонали, выигрывает.")
    time.sleep(3.5)
    print()
    print("Например:")
    print()
    time.sleep(2)
    print("   | 0 | 1 | 2 |         | 0 | 1 | 2 |         | 0 | 1 | 2 |")
    print("  --------------        --------------        --------------")
    print(" 0 | X | X | X |       0 | X  |   |  |       0 | X  |   |  |")
    print("  --------------        --------------        --------------")
    print(" 1 |   |   |   |       1 |   | X |   |       1 | X |   |   |")
    print("  --------------        --------------        --------------")
    print(" 2 |   |   |   |       2 |   |   | X |       2 | X |   |   |")
    print("  --------------        --------------        --------------")
    time.sleep(5)
    print()
    print("Первый ход делает игрок, ставящий крестики.")
    print()
    time.sleep(2)
    print("Для того, чтобы сделать ход, нужно ввести цифрами через пробел, номер строки и номер столбца выбранной вами клетки")
    print()
    time.sleep(3)
    print("Например: 1 2")
    print()
    time.sleep(3)
    print("   | 0 | 1 | 2 |")
    print("  --------------")
    print(" 0 |   |   |   |")
    print("  --------------")
    print(" 1 |   |   | X |")
    print("  --------------")
    print(" 2 |   |   |   |")
    print("  --------------")
    time.sleep(4)
    print("-----------------------")
    print("Приступаем к игре!")

time.sleep(1.5)
print("Если вы не знакомы с правилами игры, рекомендуем пройти обучение")
print()
time.sleep(1.5)

def tutorial():                           # Обучение
    while True:
        tutorial_input = input("Вы согласны пройти обучение? Введите Y/N:").upper()
        if tutorial_input == "Y":
            print()
            print("Вы согласились пройти обучение")
            print()
            time.sleep(0.8)
            rules()
            break
        elif tutorial_input == "N":
            print()
            print("Вы откализись от обучения, приступаем к игре!")
            print("---------------------------------------------")
            break
        else: print("Вы ввели неверные данные, попробуйте ещё раз")
    time.sleep(3)

tutorial()

field = [[" "] * 3 for i in range(3) ]  # создаем игровое поле
print()

def check_win():                        # проверка выйгрыша
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            print()
            show()
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            print()
            show()
            return True
    return False

def show():                             # показываем игровое поле
    print("   | 0 | 1 | 2 |")
    print("  --------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(map(str, row))} |"
        print(row_str)
        print("  --------------")
    print()
show()

def check():                            # проверяем ход игрока
    while True:
        cords = input("    Ваш Ход: ").split()

        if len(cords) !=2:
            print("Введите 2 координаты!")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] !=" ":
            print("Клетка занята! ")
            continue

        return x, y

stroke_num = 0
while True:                             # определяем номер хода
    stroke_num += 1

    show()

    if stroke_num % 2 == 1:
        print(" Ходит Крестик ")
    else:
        print(" Ходит Нолик ")

    x, y = check()

    if stroke_num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if stroke_num == 9:
        break
        print(" Ничья ")
