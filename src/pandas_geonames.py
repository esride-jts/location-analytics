import pandas as pd

class Geonames:
    """Geonames datasource represents Gazetteer data."""

    def __init__(self):
        self._data = None
        self._delimiter = "\t"
        self._header = None
        self._columns = ["geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude", "feature_class", "feature_code", "country_code", "alternate_country_code", "admin1_code", "admin2_code", "admin3_code", "admin4_code", "population", "elevation", "dem", "timezone", "modification_date"]

    def __del__(self):
        del self._data
            


    def read(self, file_path):
        """Reads the specified file into a pandas dataframe."""
        self._data = pd.read_csv(file_path, delimiter=self._delimiter, header=self._header, names=self._columns, low_memory=False)

    def last_updates(self):
        """Returns the records having the youngest update timestamp."""
        assert(self._data is not None), "The geonames data must be read into memory before getting queried!"

        latest_update = self._data["modification_date"].max()
        return self._data.loc[latest_update == self._data["modification_date"]]