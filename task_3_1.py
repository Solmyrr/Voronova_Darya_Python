def num_translation(translation=input("Введите число от 1 до 10 на английском: ")):
    numbers = {
        "one": "один",
        "two": 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    for key in numbers:
        if translation == key:
            num = numbers.setdefault(key)
            print(num)
        else:
            None

num_translation()

# Больше времени ушло на написание тела функции, чем на нее саму.