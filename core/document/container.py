import json
from typing import List

from settings import STORAGE_DIR


class Document:
    _d_id = 1

    def __init__(self, reference: str, doc_id: str = None):
        self._doc_id = Document.assign_new_id() if doc_id is None else doc_id
        self._doc_ref = reference

    @classmethod
    def assign_new_id(cls) -> str:
        _id = str(cls._d_id)
        cls._d_id += 1
        return _id

    @property
    def doc_id(self) -> str:
        return str("doc_" + self._doc_id)

    @property
    def doc_reference(self):
        return self._doc_ref

    def serialize_data(self):
        return {"id": self._doc_id, "reference": self._doc_ref}

    def load(self, d_id, reference):
        self._doc_id = d_id
        self._doc_ref = reference


class DocumentManager:
    def __init__(self):
        self._docs = list()
        self._file_name = "doc_mg42.json"
        self._save_path = STORAGE_DIR.joinpath("documents")
        self._save_path.mkdir(exist_ok=True)
        self._save_path = self._save_path.joinpath(self._file_name)

    def load(self):
        if self._save_path.is_file():
            with open(self._save_path, 'r') as file:
                data = json.load(file)

            for _, value in data.items():
                _d = Document(reference=value.get("reference"), doc_id=value.get("id"))
                self._docs.append(_d)

    def save(self):
        data = dict()
        for _doc in self._docs:
            data[_doc.doc_id] = _doc.serialize_data()

        print(data)
        data = json.dumps(data)
        with open(self._save_path, 'w') as f:
            f.write(data)

    def assign_new_doc(self, doc: Document):

        self._docs.append(doc)

    def _find(self, _doc_id: str):
        _d = None

        for _doc in self._docs:
            if _doc.dock_id == _doc_id:
                _d = _doc
                break
        return _d

    def find_docs(self,docs_id:List[str])->List[Document]:
        ans = list()
        for _i in docs_id:
            if self._find(_i) is not None:
                ans.append()
