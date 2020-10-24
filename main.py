import pygame
from renderer import Renderer
from config import GameConfig
from paddle import Paddle
from eventhandler import EventHandler
from keyreader import KeyReader
import rx
from rx.subject import BehaviorSubject

config = GameConfig()
renderer = Renderer(config)
eventHandler = EventHandler()
keyReader = KeyReader()

paddle = Paddle(10000)

renderer.initialize()
renderer.register(paddle)

frameInterval = 1 / 60

def actionHandler(x):
    keys = list(keyReader.getKeyPress())

    if len(keys) > 0:
        singleKey = keys[0]
        if singleKey.code in config.controls:
            action = config.controls[singleKey.code]

            if action == 'left_up':
                paddle.moveUp()
            elif action == 'left_down':
                paddle.moveDown()

rx.interval(frameInterval).subscribe(actionHandler)

while(True):
    if not eventHandler.listen():
        break

    renderer.draw()

renderer.cleanup()