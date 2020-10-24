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

paddle_player1 = Paddle(config.sHeight)

renderer.initialize()
renderer.register(paddle_player1)

frameInterval = 1 / 60

def actionHandler(x):
    keys = list(keyReader.getKeyPress())
    codes = repr(list(map(lambda key: key.code, keys)))

    if codes in config.controls:
        action = config.controls[codes]

        if action == 'left_up':
            paddle_player1.moveUp()
        elif action == 'left_down':
            paddle_player1.moveDown()

rx.interval(frameInterval).subscribe(actionHandler)

while(True):
    if not eventHandler.listen():
        break

    renderer.draw()

renderer.cleanup()