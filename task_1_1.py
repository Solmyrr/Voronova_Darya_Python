duration = int(input("Выведите время в секундах: "))
while duration > 0:
    d = duration // 86400
    h = (duration - (d * 86400)) // 3600
    min = (duration - (d * 86400) - (h * 3600)) // 60
    sec = (duration - (d * 86400) - (h * 3600) - (min * 60))
    if min == 0 and h == 0 and d == 0:
        print(sec, "сек")
    elif h == 0 and d == 0:
        print(min, 'мин', sec, "сек")
    elif d == 0:
        print(h, "час", min, 'мин', sec, "сек")
    else:
        print(d, "дн", h, "час", min, 'мин', sec, "сек")
    duration = int(input("Выведите время в секундах: "))

# Задание не очень сложная.
# Решила добавить цикл.