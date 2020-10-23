from element import Element, ElementState

class Paddle(Element):
    def __init__(self, boundary):
        super().__init__('rect', [0, 0, 20, 200], 20, 200)
        self.boundary = boundary

        self.step = 30

    def moveUp(self):
        prev = self.state.value
        next = ElementState(prev.x, prev.y - self.step if prev.y - self.step >= 0 else prev.y)
        super().setState(next)
    
    def moveDown(self):
        prev = self.state.value
        super().setState(ElementState(prev.x, prev.y + self.step if prev.y <= self.boundary else 0))