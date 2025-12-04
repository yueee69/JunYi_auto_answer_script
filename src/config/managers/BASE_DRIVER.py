import threading
import json

class BaseDriver:
    _lock = threading.Lock()
    _cache = {}
    def __init__(self):
        self.path = None

    def load_json(self):
        with self._lock:
            if self.path not in self._cache:
                with open(self.path, 'r', encoding='utf-8') as file:
                    self._cache[self.path] = json.load(file)

    def dump_json(self):
        with self._lock:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(self._cache.get(self.path, {}), file, ensure_ascii = False, indent = 4)
