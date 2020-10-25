from rx.subject import BehaviorSubject
import uuid

class ElementState:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Element:
    def __init__(self, shape, dimensions, width, height):
        self.shape = shape
        self.dimensions = dimensions
        self.width = width
        self.height = height
        self.state = BehaviorSubject(ElementState(0,0))
        self.id = uuid.uuid4()
    
    def setState(self, state: ElementState):
        self.state.on_next(state)