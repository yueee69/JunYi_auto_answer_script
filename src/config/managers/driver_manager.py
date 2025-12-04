from .BASE_DRIVER import BaseDriver

class DriverManager(BaseDriver):
    def __init__(self):
        super().__init__()
        self.path = 'config/app/driver.json'
        self.load_json()

    def get_driver(self):
        return self._cache.get(self.path, {})["driver"]