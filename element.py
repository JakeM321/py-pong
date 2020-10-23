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
        self.state = ElementState(0,0)
    
    def setState(self, state: ElementState):
        self.state = state