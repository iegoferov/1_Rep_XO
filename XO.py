# Функция ввода номера строки и номера столбца + проверка введенного числа и диапазано.
def vvod():
    if count_xory % 2 != 0:
        print('Ход игрока X')
    else:
        print('Ход игрока Y')
# Ввод номера строки и номера столбца
    while True:
        x_y_list = input('Введите через пробел номер строки и номер столбца ').split()
# Проверки, что введено 2 числа через пробел
        if len(x_y_list) != 2:
            print('Введите ДВА числа через пробел')
            continue
        if not x_y_list[0].isdigit() or not x_y_list[1].isdigit():
            print('Введите ЧИСЛА через пробел')
            continue
        if not 0 <= int(x_y_list[0]) <= 2 or not 0 <= int(x_y_list[1]) <= 2:
            print('Введите числа от 0 до 2')
            continue
        x, y = int(x_y_list[0]), int(x_y_list[1])
# Проверяем, что поле занято
        if board[x+1][y+1] != "-":
            print(" Клетка занята! ")
            continue
        return x, y

# Функция вывода игрового поля
def board_d():
    for i, row in enumerate(board):
        row_str = ' '.join(map(str, row))
        print((row_str))
# Функция проверки результата
def result():
    board_short = [[board[i][j] for j in range(1, len(board))] for i in range(1, len(board))]
    board_trans = [[board_short[j][i] for j in range(len(board_short))] for i in range(len(board_short[0]))]
    for str_l in range(len(board_short)):
        if board_short[str_l] == ['X', 'X', 'X'] or board_trans[str_l] == ['X', 'X', 'X']:
            print('Игрок X победил')
            return True
        elif board_short[str_l] == ['O', 'O', 'O'] or board_trans[str_l] == ['O', 'O', 'O']:
            print('Игрок O победил')
            return True
    if [board_short[0][0], board_short[1][1], board_short[2][2]] == ['X', 'X', 'X']:
        print('Игрок X победил')
        return True
    elif [board_short[0][2], board_short[1][1], board_short[2][0]] == ['X', 'X', 'X']:
        print('Игрок X победил')
        return True
    elif [board_short[0][0], board_short[1][1], board_short[2][2]] == ['O', 'O', 'O']:
        print('Игрок O победил')
        return True
    elif [board_short[0][2], board_short[1][1], board_short[2][0]] == ['O', 'O', 'O']:
        print('Игрок O победил')
        return True

# Основное тело программы
print('Игра крестики - нолики')
board = [[' ', 0, 1, 2]] + [[i] + ['-'] * 3 for i in range(3)]
result()
count_xory = 1

while True:
    board_d()
    x, y = vvod()
    if count_xory % 2 != 0:
        board[x+1][y+1] = 'X'
    else:
        board[x+1][y+1] = 'O'
    if result():
        board_d()
        break
    count_xory += 1
    if count_xory > 9:
        print('Ничья! Конец игры')
        break