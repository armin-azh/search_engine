from core.manager.collection import CollectionManager


class Document:
    _d_id = 1

    def __init__(self, reference: str):
        self._doc_id = Document.assign_new_id()
        self._doc_ref = reference

    @classmethod
    def assign_new_id(cls) -> str:
        _id = str(cls._d_id)
        cls._d_id += 1
        return _id

    @property
    def doc_id(self) -> str:
        return str("doc_" + self._doc_id)

