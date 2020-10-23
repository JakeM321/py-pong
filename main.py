import pygame
from renderer import Renderer
from config import GameConfig
from element import ElementState, Element
from eventhandler import EventHandler

config = GameConfig()
renderer = Renderer(config)
eventHandler = EventHandler()

paddle = Element('rect', [0, 0, 20, 200], 20, 200)
paddle.setState(ElementState(0, 0))

renderer.initialize()
renderer.register(paddle)

paddle.setState(ElementState(50, 50))

running = True

while(running):
    running = eventHandler.listen()
    renderer.draw()

renderer.cleanup()