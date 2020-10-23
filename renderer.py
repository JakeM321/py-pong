import pygame
from config import GameConfig, Colours
from element import Element

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colors: Colours, element: Element):
        super().__init__()

        self.image = pygame.Surface([element.width, element.height])
        self.image.fill(colors.background)
        self.image.set_colorkey(colors.background)

        if element.shape == 'rect':
            pygame.draw.rect(self.image, colors.primary, element.dimensions)
            self.rect = self.image.get_rect()
            self.rect.x = element.state.x
            self.rect.y = element.state.y

class Renderer:
    def __init__(self, config: GameConfig):
        self.config = config
    
    def initialize(self):
        self.screen = pygame.display.set_mode(self.config.dimensions)
        pygame.display.set_caption(self.config.caption)
        self.sprites = pygame.sprite.Group()

    def register(self, element: Element):
        sprite = Sprite(self.config.colours, element)
        self.sprites.add(sprite)

    def draw(self):
        self.screen.fill(self.config.colours.background)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()