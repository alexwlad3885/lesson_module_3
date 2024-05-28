#   Дополнительное практическое задание по модулю: "Подробнее о функциях."


def sum_number_and_line(list_):
    global summator
    summator = 0

    def list_unpacking(params_1):
        s: int = 0
        if isinstance(params_1, int):
            s += int(params_1)
        return s

    def dict_unpacking(**params_2):
        s: int = 0
        for k in params_2.keys():
            if isinstance(k, str):
                s += len(k)
        for v in params_2.values():
            if isinstance(v, int):
                s += int(v)
        return s

    def str_unpacking(params_3):
        s: int = 0
        if isinstance(params_3, str):
            s += len(params_3)
        return s

    def int_unpacking(params_4):
        s: int = 0
        if isinstance(params_4, int):
            s += int(params_4)
        return s

    def tuple_unpacking(params_5):
        s: int = 0
        if not isinstance(params_5, tuple) or params_5 != ():
            pass
        if isinstance(params_5, int):
            s += int(params_5)
        if isinstance(params_5, str):
            s += len(params_5)
        return s

    for i in list_:

        #   подсчет по списку

        if isinstance(i, list):
            for j in i:
                list_unpacking(j)
                summator += list_unpacking(j)

        #   подсчет по словарю

        if isinstance(i, dict):
            dict_unpacking(**i)
            summator += dict_unpacking(**i)

        #   подсчет по строке

        if isinstance(i, str):
            summator += str_unpacking(i)

        #   подсчет по кортежу

        if isinstance(i, tuple):
            for j_tuple in i:

                if isinstance(j_tuple, int):
                    int_unpacking(j_tuple)
                    summator += int_unpacking(j_tuple)

                if isinstance(j_tuple, dict):
                    dict_unpacking(**j_tuple)
                    summator += dict_unpacking(**j_tuple)

                if isinstance(j_tuple, tuple):
                    tuple_unpacking(j_tuple)
                    summator += tuple_unpacking(j_tuple)

                if isinstance(j_tuple, list):
                    j_tuple_2 = 0
                    j_tuple_3 = 0
                    j_tuple_4 = 0
                    for j_tuple_2 in range(len(j_tuple)):
                        j_tuple_dub = tuple(*j_tuple[j_tuple_2])

                        for j_tuple_3 in range(len(j_tuple_dub)):
                            if not isinstance(j_tuple_dub[j_tuple_3], tuple):
                                tuple_unpacking(j_tuple_dub[j_tuple_3])
                                summator += tuple_unpacking(j_tuple_dub[j_tuple_3])
                            else:
                                for j_tuple_4 in range(len(j_tuple_dub[j_tuple_3])):
                                    tuple_unpacking(j_tuple_dub[j_tuple_3][j_tuple_4])
                                    summator += tuple_unpacking(j_tuple_dub[j_tuple_3][j_tuple_4])

    return summator
#   конец фукции

#   начало расчетов

data_structure = [[1, 2, 3], \
                  {'a': 4, 'b': 5}, \
                  (6, {'cube': 7, 'drum': 8}), \
                  "Hello", \
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

print("результат: ", sum_number_and_line(data_structure))
