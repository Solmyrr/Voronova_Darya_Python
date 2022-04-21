phraze = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(phraze)
numbers = []
for word in phraze:
    if word.isdigit():
        numbers.extend(f'"{int(word):02}"')
    elif word.startswith('+') or word.startswith('+') and word[1].isdigit():
        numbers.extend(f'"{word[0]}{int(word):02}"')
    else:
         numbers.append(word)
edit_phraze = " ".join(numbers)
print(edit_phraze)
for





# hour = 5
# min = 17
# temp = 5
# fraze = f'в "{hour:02d}" часов "{min}" минут температура воздуха была "+{temp:02d}" градусов'


# пока не совсем понимаю, какими методами можно решать дз. Сделала в лоб. Думаю, что неправильно.
# хотелось бы разбирать на уроке задачи хотя бы отдаленно напоминающие ДЗ по уровню сложности,
# чтобы выработать какой-то алгоритм действий
# Ощущаю растерянность перед выполнением заданий. Как буд-то патроны дали, а ружье забыли :)