prices = [53.2, 42.3, 45.8, 0.6, 78.26, 25.12, 87.6, 47.16]
for price in prices:
    rub = int(price)
    kop = (price - int(price)) * 100
    print(f'{rub:02} руб., {kop:02.0f} коп.', end=', ')
    continue
print(id(prices))
prices.sort()

for price in prices:
    rub = int(price)
    kop = (price - int(price)) * 100
    print(f'{rub:02} руб., {kop:02.0f} коп.', end=', ')
prices.sort(reverse=True)
print(id(prices))

# задание интересное. Если не комментировать предыдущие части кода, то end объединяет строку с предыдущей. Как это исправить?