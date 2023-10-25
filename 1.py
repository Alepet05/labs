import random

n = random.randint(4, 30)
print(f'Кол-во камней: {n}')
move = 1
while True:
    if move % 2 != 0:
        try:
            count = int(input('Возьмите 1, 2 или 3 камня: '))
        except ValueError:
            print('некорректный ввод')
            exit()

        if count < 1 or count > 3:
            print('недопустимое число')
            exit()

        if count > n:
            print('вы не можете взять столько камней')
            exit()

        n -= count
        if n <= 1:
            print('Вы победили')
            break
        print(f'\nВы взяли камней: {count}\nОставшиеся камни: {n}\n')
    else:
        count = random.randint(1, 3)
        n -= count
        if n <= 1:
            print('Победил компьютер')
            break
        print(f'Компьютер взял камней: {count}\nОставшиеся камни: {n}\n')
    move += 1
