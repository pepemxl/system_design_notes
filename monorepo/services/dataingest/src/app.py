from kv.engine import KeyValueStore


if __name__=='__main__':
    kv_store = KeyValueStore()
    kv_store.set("id", "123")
    kv_store.set("key_01", 100)
    kv_store.set("key_02", "Example of Text")
    # Checaremos que funciona el get
    print("Name:", kv_store.get("id"))
    print("Age:", kv_store.get("key_01"))
    print("City:", kv_store.get("key_02"))
    kv_store.delete("id")
    # Try to access the deleted key
    print("Age after deletion:", kv_store.get("age"))
