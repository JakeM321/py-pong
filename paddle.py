from element import Element

class Paddle(Element):
    def __init__(self, boundary, initX, initY):
        super().__init__('rect', [0, 0, 20, 200], 20, 200)
        self.boundary = boundary - 200

        self.step = 30
        self.setPosition((initX, initY))

    def moveUp(self):
        prev = self.position.value
        next = (prev[0], prev[1] - self.step if prev[1] - self.step >= 0 else prev[1])
        super().setPosition(next)
    
    def moveDown(self):
        prev = self.position.value
        super().setPosition((prev[0], prev[1] + self.step if prev[1] <= self.boundary else prev[1]))