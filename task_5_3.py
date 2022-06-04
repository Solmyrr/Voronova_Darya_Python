tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = [ '9А', '7В', '9Б', '9В', '8Б',]


def puple_class(tutors, groups):
    idx = 0
    for idx, tutor in enumerate(tutors):
        if idx < len(groups):
            yield tutor, groups[idx]
            idx += 1

        else:
            yield tutor, None

x = puple_class(tutors, groups)

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = [ '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def puple_class_2(tutors, groups):
    idx = 0
    for idx, tutor in enumerate(tutors):
        if idx < len(groups):
            yield tutor, groups[idx]
            idx += 1

        else:
            yield tutor, None

y = puple_class(tutors, groups)