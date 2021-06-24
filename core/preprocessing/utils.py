
def intersect(list1: list, list2: list) -> list:
    """
    intersect two list
    :param list1:
    :param list2:
    :return:
    """
    _i = 0
    _j = 0
    inter = list()
    while _i < len(list1) and _j < len(list2):
        if list1[_i] == list2[_j]:
            inter.append(list1[_i])
            _i += 1
            _j += 1
        elif list1[_i] < list2[_j]:
            _i += 1
        else:
            _j += 1
    return inter


def union(list1: list, list2: list) -> list:
    """
    union 2 list
    :param list1:
    :param list2:
    :return: a sorted list
    """
    _c = list()
    _c.extend(list1)
    _c.extend(list2)
    _c = set(_c)
    return sorted(list(_c))


def tokenizer(seq: str, strip_char: str, stop_word: list) -> list:
    """
    tokenize word base on the stop word and strip char
    :param seq:
    :param strip_char:
    :param stop_word:
    :return: list of tokens
    """
    seq = seq.split(" ")
    seq_split = list()

    for s in seq:
        if len(s.splitlines()) > 1:
            for i in s.splitlines():
                if i not in stop_word:
                    seq_split.append(i)
        else:
            if s not in stop_word:
                seq_split.append(s)
    seq = [i.strip(strip_char).lower() for i in seq_split if i.strip(strip_char) != '']
    return seq
