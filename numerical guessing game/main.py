from random import randint

print("Добро пожаловать в числовую угадайку")

def max_range():
    while True:
        max_num = input("Введите максимальное целое число для верхней границы диапазона: ")
        if max_num.isdigit() and int(max_num) > 0:
            return int(max_num)
        else:
            print('Введите целое число больше нуля!')

def is_valid(s, max_num):
    return s.isdigit() and 1 <= int(s) <= max_num

def input_num(max_num):
    while True:
        guess = input(f"Введите число от 1 до {max_num}: ")
        if is_valid(guess, max_num):
            return int(guess)
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

def restart_game():
    while True:
        replay = input("Хотите начать сначала? (Введите ДА или НЕТ): ")
        if replay.lower() == "да":
            compare_num()
        elif replay.lower() == "нет":
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return False
        else:
            print("А может быть все-таки введем ДА или НЕТ?")

def compare_num():
    max_num = max_range()
    num = randint(1, max_num)
    cnt_guess = 1
    while True:
        n = input_num(max_num)
        if n < num:
            cnt_guess += 1
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif n > num:
            cnt_guess += 1
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            print("Ваше количество попыток:", cnt_guess, "\n")
            if not restart_game():
                break

compare_num()
