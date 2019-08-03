import os
import unittest

if __name__ == '__main__':
    print("Location Analytics")

    # Setup default file paths
    os.environ["geonames_file_path"] = "~/Data/DE.txt"

    unittest.main("pandas_testing", exit=False)