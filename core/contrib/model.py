from core.preprocessing.preprocessor import SamplePreProcessor
from core.indexer.constructor import SampleIndexer
from core.manager.collection import CollectionManager
from core.document.container import DocumentManager, Document

from settings import STORAGE_DIR

import tqdm
import json
import pathlib
import pickle


class SampleModel:
    def __init__(self):
        self._p_processor = SamplePreProcessor()
        self._indexer = SampleIndexer()
        self._col_manager = CollectionManager()
        self._doc_manager = DocumentManager()

    def build(self):
        self._doc_manager.assign_new_doc(Document(reference="ar,om"))

        self._doc_manager.save()


if __name__ == '__main__':
    model = SampleModel()
    model.build()
