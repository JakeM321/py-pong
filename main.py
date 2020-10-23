import pygame
from renderer import Renderer
from config import GameConfig
from paddle import Paddle
from eventhandler import EventHandler
import rx
from rx.subject import BehaviorSubject

config = GameConfig()
renderer = Renderer(config)
eventHandler = EventHandler()

paddle = Paddle(10000)

renderer.initialize()
renderer.register(paddle)

g = BehaviorSubject(True)

def movePaddle(x):
    if (paddle.state.value.y > 1000):
        g.on_next(False)

    if (paddle.state.value.y <= 0):
        g.on_next(True)

    if (g.value == True):
        paddle.moveDown()
    else:
        paddle.moveUp()

frameInterval = 1 / 60

rx.interval(frameInterval).subscribe(movePaddle)

while(True):
    if not eventHandler.listen():
        break

    renderer.draw()

renderer.cleanup()