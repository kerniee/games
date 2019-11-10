import globals
import pygame as pg
from pygame.math import Vector2 as Vector
from objects import Body
from data import *
#from sys import maxsize
from collections import deque


pg.init()
globals.init()
size = width, height = globals.SIZE

screen = pg.display.set_mode(size)
planets = get_solar_system()
for planet in planets:
    planet.surface = screen
running = True

clock = pg.time.Clock()

average_perc = 5
last_frames = deque()
average_fps = 0
physic_tick = 1
level_of_tick_change = 10

while running:
    fps = clock.get_fps()
    #print(fps)
    if len(last_frames) == average_perc-1 and fps != 0:
        average_fps = sum(last_frames) / len(last_frames)
        if average_fps > globals.FPS:
            physic_tick += 1
        elif average_fps < globals.FPS:
            physic_tick -= 1
        last_frames = deque()
    elif fps != 0:
        last_frames.append(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        #print(event)
        if event.type == pg.KEYDOWN:
            if event.dict['unicode'] == '1':
                globals.TIMESTEP = 60
            if event.dict['unicode'] == '2':
                globals.TIMESTEP = 60*6
            if event.dict['unicode'] == '3':
                globals.TIMESTEP = 60*24

        if event.type == pg.MOUSEBUTTONUP:
            button = event.dict['button']

            # WheelDown
            if button == 5:
                globals.SCALE *= globals.SCROLL_SCALE

            # WheelUp
            if button == 4:
                globals.SCALE /= globals.SCROLL_SCALE

    screen.fill((0, 0, 0))
    times = int((average_fps // 60)+physic_tick)
    for t in range(times):
        for i, planet in enumerate(planets):
            for j in range(i+1, len(planets)):
                planets[j] = planet.apply_force(planets[j])
                planets[j].move(globals.TIMESTEP)
            planet.move(globals.TIMESTEP)
            planet.acc = Vector(0)

    for planet in planets:
        if planet.in_outer_space():
            planets.remove(planet)
            continue
        planet.draw()

    pg.display.flip()
    clock.tick()
    #print(average_fps)


pg.quit()
