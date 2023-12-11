import unittest
if __name__=='__main__':
    import os
    import sys
    temp_path = os.path.dirname(os.path.abspath(__file__))
    temp_path = os.path.dirname(temp_path)
    sys.path.append(temp_path)
# from monorepo.services.dataingest.src.kv.engine import KeyValueStore
# from monorepo.services.dataingest.src.kv.engine import KeyValueStore2
from kv.engine import KeyValueStore
from kv.engine import KeyValueStore2

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.kv_store = KeyValueStore()

    def test_set_and_get(self):
        self.kv_store.set("key1", "value1")
        self.assertEqual(self.kv_store.get("key1"), "value1")

    def test_set_and_get_int(self):
        self.kv_store.set("key_int", 10)
        self.assertEqual(self.kv_store.get("key_int"), 10)

    def test_set_and_get_float(self):
        self.kv_store.set("key_float", 10.5)
        self.assertEqual(self.kv_store.get("key_float"), 10.5)

    def test_set_and_get_array(self):
        self.kv_store.set("key_array", [1, 2, 3, 4, 5])
        self.assertEqual(self.kv_store.get("key_array"), [1, 2, 3, 4, 5])

    def test_set_and_delete(self):
        self.kv_store.set("key2", "value2")
        self.kv_store.delete("key2")
        self.assertIsNone(self.kv_store.get("key2"))

    def test_delete_nonexistent_key(self):
        self.assertRaises(KeyError, self.kv_store.delete, "nonexistent_key")

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.kv_store.get("nonexistent_key"))


class TestKeyValueStore2(unittest.TestCase):
    def setUp(self):
        self.kv_store = KeyValueStore2()

    def test_set_and_get(self):
        self.kv_store.set("key1", "value1")
        self.assertEqual(self.kv_store.get("key1"), "value1")

    def test_set_and_delete(self):
        self.kv_store.set("key2", "value2")
        self.kv_store.delete("key2")
        self.assertIsNone(self.kv_store.get("key2"))

    def test_delete_nonexistent_key(self):
        self.assertRaises(KeyError, self.kv_store.delete, "nonexistent_key")

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.kv_store.get("nonexistent_key"))


if __name__ == '__main__':
    unittest.main()
