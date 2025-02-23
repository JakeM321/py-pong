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

# Bug - ball bounces the wrong way and passes through the paddle when hitting the top of it

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
    ballHitFloorOrCeiling = ball.position.value[1] <= yMin or ball.position.value[1] >= yBoundary
    ballOutOfBounds = ball.position.value[0] <= xMin or ball.position.value[0] >= xBoundary

    if ballHitPaddle or ballHitFloorOrCeiling:
        ball.handleCollision(ballHitFloorOrCeiling)
    
    if ballOutOfBounds:
        time.sleep(2)
        ball.setPosition((xMin + 30, yBoundary - 50))
        ball.handleCollision(False)

    ball.lapse()

continueRunning = True

while(continueRunning):
    handleActions()

    if not eventHandler.quit():
        continueRunning = False
        renderer.cleanup()

    renderer.draw(store)
    time.sleep(1 / fps)
