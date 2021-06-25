from core.posting.container import SamplePosting


class Indexer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        raise NotImplementedError("This method should be implemented")


class SampleIndexer(Indexer):
    def __init__(self, *args, **kwargs):
        self._hash_dic = dict()
        super(SampleIndexer, self).__init__(*args, **kwargs)

    def __setitem__(self, key: str, value: str):
        """
        :param key: term
        :param value: doc_id
        :return:
        """
        if self._hash_dic.get(key) is None:
            _n = SamplePosting()
            _n.assign_doc(value)
            self._hash_dic[key] = _n

        else:
            self._hash_dic[key].assign_doc(value)

    def get(self, key):
        return self._hash_dic[key] if self._hash_dic.get(key) is not None else None



