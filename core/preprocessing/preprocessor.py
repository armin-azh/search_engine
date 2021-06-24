from typing import List
from stop_word import EN_STOP_WORDS
import nltk


class Preprocessor:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, seq: str) -> List[str]:
        raise NotImplementedError("This method should be implemented")


class SamplePreProcessor(Preprocessor):
    """
    a sample preprocessor on english text
    """

    def __init__(self, *args, **kwargs):
        self._stop_word = EN_STOP_WORDS
        self._strip_char = "`@!?,.\n"
        self._porter = nltk.PorterStemmer()

        super(SamplePreProcessor, self).__init__(*args, **kwargs)

    def _tokenizer(self, seq: str):
        """
        generate tokens
        :param seq:
        :return:
        """
        seq = seq.split(" ")

        for s in seq:
            if len(s.splitlines()) > 1:
                for i in s.splitlines():
                    if i.lower() not in self._stop_word:
                        yield i.lower()
            else:
                if s.lower() not in self._stop_word:
                    yield s.lower()

    def _strip(self, token: str) -> str:
        return token.strip(self._strip_char).lower()

    def _porter_stemmer(self, token: str) -> str:
        return self._porter.stem(token)

    def process(self, seq: str) -> List[str]:

        ls = list()
        for token in self._tokenizer(seq):

            # operator
            token = self._porter_stemmer(token)
            token = self._strip(token)
            if token != '':
                ls.append(token)
        return ls

