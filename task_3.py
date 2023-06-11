print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


def flipping(numm):
  new_numm = 0
  summ_flipping = 0
  while numm > 0:
    new_numm = numm % 10
    summ_flipping *= 10
    summ_flipping = summ_flipping + new_numm
    numm //= 10
  return summ_flipping


def main():
  print("===Меню программы===\n")
  try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))

    print("\nПервое число наоборот: ", flipping(first_number))
    print("Второе число наоборот:", flipping(second_number))

    summ = flipping(first_number) + flipping(second_number)

    print("Сумма: ", summ)
    print("\nСумма наоборот: ", flipping(summ))
  except ValueError:
    print(
      "\n===Ошибка! Были введены символы, а не число.===\nПовторите попытку\n")
    main()


main()
