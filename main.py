import pygame
from renderer import Renderer
from config import GameConfig
from paddle import Paddle
from eventhandler import EventHandler
from keyreader import KeyReader
import rx
from rx.subject import BehaviorSubject
import time

config = GameConfig()
renderer = Renderer(config)
eventHandler = EventHandler()
keyReader = KeyReader()

paddle_player1 = Paddle(config.sHeight, 0, 0)
paddle_player2 = Paddle(config.sHeight, config.sWidth - 20, 0)

renderer.initialize()
renderer.register(paddle_player1)
renderer.register(paddle_player2)

timelapse = 1 / 100
fps = 120

def actionHandler(x):
    keys = list(keyReader.getKeyPress())
    codes = list(map(lambda key: key.code, keys))
    actions = list(map(lambda code: config.controls[code],
        filter(lambda code: code in config.controls, codes)))

    if 'left_up' in actions:
        paddle_player1.moveUp()
    if 'left_down' in actions:
        paddle_player1.moveDown()
    if 'right_up' in actions:
        paddle_player2.moveUp()
    if'right_down' in actions:
        paddle_player2.moveDown()

rx.interval(timelapse).subscribe(actionHandler)

while(True):
    if not eventHandler.listen():
        break

    renderer.draw()
    time.sleep(1 / fps)

renderer.cleanup()