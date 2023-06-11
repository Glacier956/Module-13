print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.


def maximum_of_two(first_number, second_number):
  return first_number if first_number > second_number else second_number


def maximum_of_three(first_number, second_number, third_number):
  return maximum_of_two(maximum_of_two(first_number, second_number),
                        maximum_of_two(second_number, third_number))


def main():
  print("===Меню программы===\n")
  try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    third_number = int(input("Введите третье число: "))

    print("\nМаксимум из трёх чисел равно",
          maximum_of_three(first_number, second_number, third_number))
  except ValueError:
    print(
      "\n===Ошибка! Были введены символы, а не число.===\nПовторите попытку\n")
    main()


main()
