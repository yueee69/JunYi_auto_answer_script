from .managers import driver_manager, answer_manager

class MainManager:
    def __init__(self):
        #app
        self.driver_manager = driver_manager.DriverManager()
        self.answer_manager = answer_manager.AnswerManager()  

        #user