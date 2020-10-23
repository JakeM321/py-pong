import pygame

class EventHandler:
    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True