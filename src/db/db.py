import json
import os


class Db(object):
    def __init__(self, path=None):
        if path is None:
            path = f'{os.path.dirname(os.path.dirname(__file__))}/data.json'

        self.path = path
        if os.path.exists(self.path):
            self.data = json.load(open(self.path, 'r'))
        else:
            self.data = {}

    def save(self):
        json.dump(self.data, open(self.path, 'w+'))
    
    def _check_key(self, key):
        assert type(key) == str, "Key must be a string"

    def set(self, key, value):
        self._check_key(key)

        self.data[key] = value

        self.save()

    def get(self, key):
        self._check_key(key)
        try: 
            return self.data[key]
        except KeyError:
            print(f"No value found for key: {key}")

    def key_exist(self, key):
        self._check_key(key)
        if key in self.data:
            return True
        return False

    def is_empty(self):
        if self.data:
            return False
        return True

    def flush(self):
        print("Flushing db...")
        self.data  = {}
        self.save()

    