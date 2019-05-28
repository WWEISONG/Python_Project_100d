def find_max(list_obj):
    """
    find max value and second max value in list
    :param list_obj: list
    :return: max, second max
    """

    if len(list_obj) == 0 or 1:
        return 'at least two elements in list.'
    m1, m2 = (list_obj[0], list_obj[1]) if list_obj[0] > list_obj[1] \
        else (list_obj[1], list_obj[0])
    for index in range(2, len(list_obj)):
        if list_obj[index] > m1:
            m2 = m1
            m1 = list_obj[index]
        elif list_obj[index] > m2:
            m2 = list_obj
    return m1, m2

if __name__ == '__main__':
    find_max(list_obj=[1, 2, 3, 4, 5, 6])