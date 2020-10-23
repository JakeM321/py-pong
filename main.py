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
        

rx.interval(0.05).subscribe(movePaddle)

running = True

while(running):
    running = eventHandler.listen()
    renderer.draw()

renderer.cleanup()