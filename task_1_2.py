my_list = []
numbers = range(1, 1001, 2)
for i in numbers:
    cube = i ** 3
    my_list.append(cube)
final_sum = 0
for num in my_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)
# эта задача показалась мне самой сложной. Пройдя 4 урока по данному курсу с другим преподавателем,
# я заморозила курс и начала его по новой с Вами.
# Мне нужно было время подчистить хвосты и разобраться в нескольких темах.
# Многое улеглось и стало более понятным,
# но списки все еще вызывают некоторые сложности





