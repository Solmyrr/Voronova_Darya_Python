people = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
names = []
for i in people:
    i = i.split(" ")[-1]
    names.append(i)
count = 0
while count < len(names):
    print("Привет, ", names[count].title(), "!", sep="")
    count += 1

