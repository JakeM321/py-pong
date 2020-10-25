import pygame
from config import GameConfig, Colours
from element import Element, ElementState
from spritestore import SpriteStore

class Renderer:
    def __init__(self, config: GameConfig):
        self.config = config
    
    def initialize(self):
        self.screen = pygame.display.set_mode(self.config.dimensions)
        pygame.display.set_caption(self.config.caption)

    def draw(self, store: SpriteStore):
        self.screen.fill(self.config.colours.background)
        store.sprites.draw(self.screen)
        pygame.display.flip()

    def cleanup(self):
        print("Cleanup")
        pygame.quit()