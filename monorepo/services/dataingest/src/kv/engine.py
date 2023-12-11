from dataclasses import dataclass, field
import json
import logging
import os
from typing import Optional
# if __name__=='__main__':
#     import os
#     import sys
#     temp_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..")
#     print(os.path.abspath(temp_path))
#     sys.path.append(temp_path)
# from monorepo.common.constants import DATA_PATH


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..", "LOCAL_DATA", "DATA")
DB_FULL_FILENAME = os.path.join(DATA_PATH, "db_kv.json")

logging.basicConfig(format='%(asctime)s :: %(message)s')
logging.getLogger().setLevel(logging.ERROR)
log = logging.getLogger(__name__)

@dataclass
class KeyValueStore:
    store: dict = field(default_factory=dict)
    db_full_filename: str = DB_FULL_FILENAME

    def set(self, key: str, value):
        self.store[key] = value

    def get(self, key: str):
        return self.store.get(key)

    def delete(self, key: str):
        try:
            del self.store[key]
        except KeyError:
            log.exception(f"Key '{key}' not found.")
            raise KeyError

    def save_to_file(self):
        with open(self.db_full_filename, 'w') as ptr_file:
            json.dump(self.store, ptr_file)

    def load_from_file(self):
        try:
            with open(self.db_full_filename, 'r') as ptr_file:
                self.store = json.load(ptr_file)
        except FileNotFoundError:
            log.exception(f"File '{self.db_full_filename}' not found.")
        except json.JSONDecodeError:
            log.exception(f"Error decoding JSON from file '{self.db_full_filename}'.")


class KeyValueStore2:
    def __init__(self, db_full_filename=DB_FULL_FILENAME):
        self.store = {}
        self.db_full_filename = db_full_filename

    def set(self, key:str, value):
        self.store[key] = value

    def get(self, key:str):
        return self.store.get(key)

    def delete(self, key):
        if key in self.store:
            del self.store[key]
        else:
            log.exception(f"Key '{key}' not found.")
            raise KeyError

    def save_to_file(self):
        with open(self.db_full_filename, 'w') as ptr_file:
            json.dump(self.store, ptr_file)

    def load_from_file(self):
        try:
            with open(self.db_full_filename, 'r') as ptr_file:
                self.store = json.load(ptr_file)
        except FileNotFoundError:
            log.exception(f"File '{self.db_full_filename}' not found.")
        except json.JSONDecodeError:
            log.exception(f"Error decoding JSON from file '{self.db_full_filename}'.")


def test_kv_class():
    # Example usage:
    kv_store = KeyValueStore2()

    kv_store.set("name", "Pepe")
    kv_store.set("city", "Mexicali")
    kv_store.set("state", "Baja California")

    log.info("Name:", kv_store.get("name"))
    log.info("City:", kv_store.get("city"))
    log.info("State:", kv_store.get("state"))

    kv_store.delete("city")
    log.info("City after deletion:", kv_store.get("city"))


def test_kv_dataclass():
    # Example usage:
    kv_store = KeyValueStore()

    kv_store.set("name", "Pepe")
    kv_store.set("city", "Mexicali")
    kv_store.set("state", "Baja California")

    log.info("Name:", kv_store.get("name"))
    log.info("City:", kv_store.get("city"))
    log.info("State:", kv_store.get("state"))

    kv_store.delete("city")
    log.info("City after deletion:", kv_store.get("city"))
    

if __name__ == '__main__':
    test_kv_dataclass()
    test_kv_class()
