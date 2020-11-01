import pygame
from element import Element
from config import GameConfig, Colours, gameConfig

class Sprite(pygame.sprite.Sprite):
    def applyStateChange(self, update):
        self.rect.x = update[0]
        self.rect.y = update[1]

    def __init__(self, colors: Colours, element: Element):
        super().__init__()

        self.image = pygame.Surface([element.width, element.height])
        self.image.fill(colors.background)
        self.image.set_colorkey(colors.background)
        self.id = element.id

        if element.shape == 'rect':
            pygame.draw.rect(self.image, colors.primary, element.dimensions)
            self.rect = self.image.get_rect()
            element.position.subscribe(self.applyStateChange)

class SpriteStore:
    def __init__(self, config: GameConfig):
        self.config = config
        self.sprites = pygame.sprite.Group()
        self.lookup = {}

    def register(self, element: Element):
        sprite = Sprite(self.config.colours, element)
        self.sprites.add(sprite)
        self.lookup[sprite.id] = sprite

store = SpriteStore(gameConfig)