import pygame
import configScreen

class Warrior(object):
    def __init__(self, x0, y0, screen):
        self.x0, self.y0, self.screen = x0, y0, screen

    def draw(self):
        head = pygame.draw.rect(self.screen, (255,255,0), pygame.Rect(self.x0, self.y0, 10, 10))
        pygame.draw.rect(self.screen, (255,255,0), head)
        pygame.display.flip()

    def move(self, axis, direction):
        if axis == "X":
            setattr(self, 'x0', (self.x0 + direction * .05)%configScreen.width)
        if axis == "Y":
            setattr(self, 'y0', (self.y0 + direction * .05)%configScreen.height)

        self.screen.fill(configScreen.background_colour)
        self.draw()