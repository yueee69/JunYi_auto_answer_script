class FakeElement:
    def __init__(self):
        self.clicked = False
        self.text = ""
    
    def click(self):
        self.clicked = True

    def send_keys(self, v):
        self.text = v

    def received(self):
        pass

class FakeDriver:
    def __init__(self, elements=None):
        self.elements_map = elements or {}

    def find_elements(self, by=None, value=None):
        return self.elements_map.get(value, [])
