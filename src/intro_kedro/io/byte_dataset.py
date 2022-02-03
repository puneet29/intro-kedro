from kedro.io.core import AbstractDataSet, DataSetError


class BinaryDataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath

    def _load(self):
        with open(str(self._filepath), "rb") as f:
            return f.read()

    def _save(self, _):
        raise DataSetError("Read only dataset")

    def _describe(self):
        return dict(filepath=self._filepath)
