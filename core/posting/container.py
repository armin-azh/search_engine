from typing import List


class Posting:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sort(self):
        raise NotImplementedError("This method should be implemented")

    @property
    def frequency(self) -> int:
        raise NotImplementedError("This method should be implemented")


class SamplePosting(Posting):
    def __init__(self, *args, **kwargs):
        self._ls = []
        self._f = 0
        super(SamplePosting, self).__init__(*args, **kwargs)

    @property
    def frequency(self) -> int:
        print(self._ls)
        return self._f

    def assign_doc(self, _doc: str):
        if _doc not in self._ls:
            self._ls += [_doc]

        self._f += 1

    def sort(self):
        self._ls.sort()

    def posting_list(self) -> List[str]:
        self.sort()
        return self._ls
