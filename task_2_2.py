phraze = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(phraze)
numbers = []
for word in phraze:
    if word.isdigit():
        numbers.extend(['"', f'{int(word):02}', '"'])
    elif (word.startswith('+') or (word.startswith('-')) and word[1:].isdigit()):
        numbers.extend(['"', f'{word[0]}{int(word[1:]):02}', '"'])
    else:
         numbers.append(word)
edit_phraze = ' '.join(numbers)
print(edit_phraze)

# Разобралась с расчленением цифр, но удалить пробелы так и не смогла...





# https: // github.com / Solmyrr / Voronova_Darya_Python / pull / 1