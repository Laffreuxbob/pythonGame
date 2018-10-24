import pygame
from math import pi
from warrior import Warrior
import configScreen as confS

print("conf : ", confS)

screen = pygame.display.set_mode((confS.width, confS.height), pygame.RESIZABLE)
screen.fill(confS.background_colour)

pygame.display.set_caption('xX_-G4M3R_0riGIin_Z0n3-_Xx')

pygame.display.flip()
running = True

c1 = Warrior(10, 10, screen)

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

