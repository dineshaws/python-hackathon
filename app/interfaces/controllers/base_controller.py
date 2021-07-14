
class BaseController():
    def __init__(self) -> None:
        pass

    def create(self):
        raise Exception('ERR_METHOD_NOT_IMPLEMENTED')
    
    def update(self):
        raise Exception('ERR_METHOD_NOT_IMPLEMENTED')

    def get(self):
        raise Exception('ERR_METHOD_NOT_IMPLEMENTED')

    def remove(self):
        raise Exception('ERR_METHOD_NOT_IMPLEMENTED')