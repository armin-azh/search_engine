EN_STOP_WORDS = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
    "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
    'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before',
    'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
    'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
    'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y',
    'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
    "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't",
    'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
]


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
