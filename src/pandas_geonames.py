import pandas as pd

class Geonames:
    """Geonames datasource represents Gazetteer data."""

    def __init__(self):
        self._delimiter = "\t"
        self._header = 0

    def read(self, file_path):
        return pd.read_csv(file_path, delimiter=self._delimiter, header=self._header, low_memory=False)