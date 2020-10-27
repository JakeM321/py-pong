import pygame
import rx
from rx.subject import BehaviorSubject
from rx import operators as op
from rx.scheduler import CurrentThreadScheduler
import time

from renderer import Renderer
from config import gameConfig
from paddle import Paddle
from eventhandler import EventHandler
from keyreader import KeyReader
from ball import Ball
from spritestore import store
from collisionchecker import collisionChecker

# TODO - upwards motion issue causing ball to pass through collision

renderer = Renderer(gameConfig)

eventHandler = EventHandler()
keyReader = KeyReader()

yBoundary = gameConfig.sHeight - 30
yMin = 30
xBoundary = gameConfig.sWidth - 30
xMin = 30

paddle_player1 = Paddle(yBoundary, xMin, yMin)
paddle_player2 = Paddle(yBoundary, xBoundary - 20, yMin)
ball = Ball(xBoundary, yBoundary, xMin, yBoundary - 50)

renderer.initialize()
store.register(paddle_player1)
store.register(paddle_player2)
store.register(ball)

fps = 60

def handleActions():
    keys = list(keyReader.getKeyPress())
    codes = list(map(lambda key: key.code, keys))
    actions = list(map(lambda code: gameConfig.controls[code],
        filter(lambda code: code in gameConfig.controls, codes)))

    if 'left_up' in actions:
        paddle_player1.moveUp()
    if 'left_down' in actions:
        paddle_player1.moveDown()
    if 'right_up' in actions:
        paddle_player2.moveUp()
    if 'right_down' in actions:
        paddle_player2.moveDown()

    ballHitPaddle = collisionChecker.check(paddle_player1, ball) or collisionChecker.check(paddle_player2, ball)
    ballHitFloorOrCeiling = ball.state.value.y <= yMin or ball.state.value.y >= yBoundary
    ballOutOfBounds = ball.state.value.x <= xMin or ball.state.value.x >= xBoundary

    if ballHitPaddle or ballHitFloorOrCeiling:
        ball.handleCollision(ballHitFloorOrCeiling)
    
    if ballOutOfBounds:
        time.sleep(2)
        ball.state.value.x = xMin + 30
        ball.state.value.y = yBoundary - 50
        ball.handleCollision(False)

    ball.lapse()

continueRunning = True

while(continueRunning):
    handleActions()

    if not eventHandler.listen():
        continueRunning = False
        renderer.cleanup()

    renderer.draw(store)
    time.sleep(1 / fps)
