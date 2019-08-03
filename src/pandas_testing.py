import os
import pandas as pd
import pandas_geonames as pd_geo
import unittest

class TestPandas(unittest.TestCase):

    geonames_file_path = os.environ.get("geonames_file_path")

    def test_read(self):
        geonames = pd_geo.Geonames()
        geonames.read(self.geonames_file_path)
        del geonames

    def test_query_lates(self):
        geonames = pd_geo.Geonames()
        geonames.read(self.geonames_file_path)
        latest_updates = geonames.last_updates()
        self.assertLess(0, len(latest_updates), "At least one record must be the latest update!")
        del geonames