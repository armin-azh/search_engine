from utils import STOP_WORDS


class Tokenizer(object):
    def __init__(self, strip_ch):
        self._strip_char = strip_ch

    def get_token(self, seq):
        seq = seq.split(" ")
        seq_split = list()

        for s in seq:
            if len(s.splitlines()) > 1:
                for i in s.splitlines():
                    if i not in STOP_WORDS:
                        seq_split.append(i)
            else:
                if s not in STOP_WORDS:
                    seq_split.append(s)
        seq = [i.strip(self._strip_char).lower() for i in seq_split if i.strip(self._strip_char) != '']
        return seq
