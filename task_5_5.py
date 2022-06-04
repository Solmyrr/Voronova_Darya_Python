src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
un_src = set()
viewed = set()
for num in src:
    if num not in viewed:
        un_src.add(num)
    else:
        un_src.discard(num)
    viewed.add(num)
print(un_src)