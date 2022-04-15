
percent = range(1, 101, 1)
for number in percent:
    if number == 11 or 10 < number <= 20:
        print(number, "процентов")
    elif number % 10 == 1:
        print(number, 'процент')
    elif 2 <= (number % 10) <= 4:
        print(number, "процента")
    else:
        print(number, "процентов")
# Задача не сложная