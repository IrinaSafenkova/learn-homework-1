"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():

    age = int(input("Введите свой возраст: "))
    if age < 7:
        print(f'Тебе еще только {age}, ходи пока в детский сад!')
    elif age >= 7 and age < 17:
        print(f'Тебе {age} лет, посещай школу.')
    elif age >= 17 and age < 23:
        print(f'Тебе {age} лет - учись в университете.')
    else:
        print(f'Тебе {age} лет, в твоем возрасте пора работать.')


if __name__ == "__main__":
    main()
