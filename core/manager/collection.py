from pathlib import Path
import pathlib
from settings import COLLECTION_DIR


class CollectionManager:
    EDITED_LABEL = 'xs1b4'
    SUFFIX = '.json'

    def __init__(self, src: Path = None):
        self._col_dir = COLLECTION_DIR if src is None else src

    def edited_label(self, col_src: Path) -> None:
        try:
            if col_src.is_file():
                col_src.rename(Path(col_src.parent, col_src.stem + "_" + self.EDITED_LABEL + col_src.suffix))
        except FileExistsError:
            print(f"[WARN] {str(col_src)} is another file and cant be renamed to it")

    @property
    def len_collections_edited(self) -> int:
        """
        get number of edited collections
        :return:
        """
        ls = self._col_dir.glob("*_" + self.EDITED_LABEL + self.SUFFIX)
        return len(list(ls))

    @property
    def len_collections(self) -> int:
        """
        get all number of collections
        :return:
        """
        return len(list(self._col_dir.glob("*.*")))

    # @property
    # def len_collections_not_edited(self)->int:
    #     """
    #     get number of collections that not edited
    #     :return:
    #     """
    #     pass

    def get_collection(self):
        """
        a generator for getting each doc what it have not edited
        :return:
        """
        for p in self._col_dir.glob("*.*"):
            if p.stem.split('_')[-1] != self.EDITED_LABEL:
                yield p

