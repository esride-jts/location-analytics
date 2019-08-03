import pandas as pd

class Geonames:
    """Geonames datasource represents Gazetteer data."""

    def __init__(self):
        self._data = None
        self._delimiter = "\t"
        self._header = 0

    def __del__(self):
        del self._data
            

    def read(self, file_path):
        """Reads the specified file into a pandas dataframe."""

        del self._data
        self._data = pd.read_csv(file_path, delimiter=self._delimiter, header=self._header, low_memory=False)