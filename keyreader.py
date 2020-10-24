import pygame

class Key:
    def __init__(self, code, label):
        self.code = code
        self.label = label

keys = {}
keys[pygame.K_w] = Key('KEY_w', 'W')
keys[pygame.K_s] = Key('KEY_s', 'S')
keys[pygame.K_UP] = Key('KEY_UP', 'Up')
keys[pygame.K_DOWN] = Key('KEY_DOWN', 'Down')

class KeyReader:
    def getKeyPress(self):
        pressedKeys = pygame.key.get_pressed()

        filtered = filter(lambda key: pressedKeys[key], keys)

        return map(lambda pyKey: keys[pyKey], filtered)