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