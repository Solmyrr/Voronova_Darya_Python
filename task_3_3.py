
name_list = ["Иван", "Мария", "Александр", "Марина", "Петр", "Ирина", "Валерия", "Виктория", "Анна"]


def thesaurus():
    name_dict = {}
    for i in name_list:
        if i[0] in name_dict:
            name_dict[i[0]].append(i)
        else:
            name_dict[i[0]] = [i]
    print(name_dict)


thesaurus()
