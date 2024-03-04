import os
import unittest
from monorepo.common.constants import LOCAL_DATA_PATH
from monorepo.common.constants import CONFIG_FILE_PATH

class ContanstsTest(unittest.TestCase):

    def test_local_path_defined(self):
        self.assertIsNotNone(LOCAL_DATA_PATH)
        flag = os.path.isdir(LOCAL_DATA_PATH)
        self.assertTrue(flag, "Folder {0} does not exist!".format(LOCAL_DATA_PATH))
    
    def test_local_config_file_exist(self):
        self.assertIsNotNone(CONFIG_FILE_PATH)
        flag = os.path.isfile(CONFIG_FILE_PATH)
        self.assertTrue(flag, "File {0} does not exist!".format(CONFIG_FILE_PATH))