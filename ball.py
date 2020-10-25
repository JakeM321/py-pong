from element import Element, ElementState

class Ball(Element):
    def __init__(self, boundaryX, boundaryY, initX, initY):
        super().__init__('rect', [0, 0, 20, 20], 20, 20)
        self.boundaryX = boundaryX - 20
        self.boundaryY = boundaryY - 20

        self.step = 15
        self.setState(ElementState(initX, initY))

        self.direction = (True, False)

    def lapse(self):
        prev = self.state.value
        next = ElementState(
            prev.x + self.step if self.direction[0] else prev.x - self.step,
            prev.y + self.step if self.direction[1] else prev.y - self.step)

        super().setState(next)

    def handleCollision(self, hAngle):
        if (hAngle):
            if (self.direction[0]):
                self.direction = (True, not self.direction[1])
            else:
                self.direction = (self.direction[0], not self.direction[1])
        else:
            if (self.direction[0]):
                self.direction = (not self.direction[0], self.direction[1])
            else:
                self.direction = (True, self.direction[1])