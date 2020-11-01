from rx.subject import BehaviorSubject
import uuid

class Element:
    def __init__(self, shape, dimensions, width, height):
        self.shape = shape
        self.dimensions = dimensions
        self.width = width
        self.height = height
        self.position = BehaviorSubject((0,0))
        self.id = uuid.uuid4()
    
    def setPosition(self, p):
        self.position.on_next(p)

