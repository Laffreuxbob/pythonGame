import pygame
from math import pi

background_colour = (0, 0, 0)

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
screen.fill(background_colour)

pygame.display.set_caption('xX_-G4M3R_0riGIin_Z0n3-_Xx')

pygame.display.flip()
running = True


class Circle(object):
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R

    def area(self):
        return pi * self.R ** 2

    def circumference(self):
        return 2 * pi * self.R

    def draw(self):
        head = pygame.draw.rect(screen, (255,255,0), pygame.Rect(self.x0, self.y0, 10, 10))
        pygame.draw.rect(screen, (255,255,0), head)
        pygame.display.flip()

    def move(self, axis, direction):
        if axis == "X":
            setattr(self, 'x0', (self.x0 + direction * .05)%width)
        if axis == "Y":
            setattr(self, 'y0', (self.y0 + direction * .05)%height)

        screen.fill(background_colour)
        self.draw()

        c1 = Circle(10, 10, 10)


c1 = Circle(10,10,10)

while running:
    c1.draw()
    pygame.display.flip()

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()  # checking pressed keys

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:

            keystate = pygame.key.get_pressed()
            while keystate[273]:
                pygame.event.get()
                keystate = pygame.key.get_pressed()
                c1.move("Y", -1)
            while keystate[274]:
                pygame.event.get()
                keystate = pygame.key.get_pressed()
                c1.move("Y", 1)
            while keystate[275]:
                pygame.event.get()
                keystate = pygame.key.get_pressed()
                c1.move("X", 1)
            while keystate[276]:
                pygame.event.get()
                keystate = pygame.key.get_pressed()
                c1.move("X", -1)

            if event.key == pygame.K_s:
                print("save")

