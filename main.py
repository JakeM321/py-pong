import pygame
from renderer import Renderer
from config import GameConfig
from paddle import Paddle
from eventhandler import EventHandler
from keyreader import KeyReader
import rx
from rx.subject import BehaviorSubject
import time
from ball import Ball
from spritestore import SpriteStore

config = GameConfig()
renderer = Renderer(config)
store = SpriteStore(config)

eventHandler = EventHandler()
keyReader = KeyReader()

paddle_player1 = Paddle(config.sHeight, 0, 0)
paddle_player2 = Paddle(config.sHeight, config.sWidth - 20, 0)
ball = Ball(config.sWidth, config.sHeight, 30, config.sHeight - 50)

renderer.initialize()
store.register(paddle_player1)
store.register(paddle_player2)
store.register(ball)

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

    #todo - collision check

    ball.lapse()

rx.interval(timelapse).subscribe(actionHandler)

while(True):
    if not eventHandler.listen():
        break

    renderer.draw(store)
    time.sleep(1 / fps)

renderer.cleanup()