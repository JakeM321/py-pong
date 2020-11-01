from element import Element

class Ball(Element):
    def __init__(self, boundaryX, boundaryY, initX, initY):
        super().__init__('rect', [0, 0, 20, 20], 20, 20)
        self.boundaryX = boundaryX - 20
        self.boundaryY = boundaryY - 20

        self.step = 15
        self.setPosition((initX, initY))

        self.direction = (True, False)

    def lapse(self):
        prev = self.position.value
        next = (
            prev[0] + self.step if self.direction[0] else prev[0]- self.step,
            prev[1] + self.step if self.direction[1] else prev[1] - self.step)

        super().setPosition(next)

    def handleCollision(self, isHorizontalAngle):
        movingRight = self.direction[0]
        movingDown = self.direction[1]

        if (isHorizontalAngle):
            self.direction = (movingRight, not movingDown)
        else:
            self.direction = (not movingRight, movingDown)