import pygame
from spritestore import SpriteStore, store
from element import Element

class CollisionChecker:
    def check(self, a: Element, b: Element):
        spriteA = store.lookup[a.id]
        spriteB = store.lookup[b.id]

        return pygame.sprite.collide_mask(spriteA, spriteB)

collisionChecker = CollisionChecker()