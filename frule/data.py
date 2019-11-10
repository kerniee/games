from globals import *
from pygame.math import Vector2 as Vector
from objects import Body
import globals

globals.init()


def get_solar_system():
    planets = []
    sun = Body('Sun', 0.0, 0.0, 0.0, 0.0)
    sun.mass = 1.98892 * 10**30
    sun.r = 695510 * 10**3
    sun.color = (255, 255, 100)
    planets.append(sun)

    merc = Body('Mercury', 0.0, 0.38 * globals.AU, 47360.0, 0.0)
    merc.mass = 3.33022 * 10**23
    merc.r = 2439.7 * 10**3
    merc.color = (100, 60, 50)
    planets.append(merc)

    venus = Body('Venus', 0.0, 0.72 * globals.AU, 35020.0, 0.0)
    venus.mass = 4.8675 * 10**24
    venus.r = 6051.8 * 10**3
    venus.color = (200, 190, 150)
    planets.append(venus)

    earth = Body('Earth', 0.0, globals.AU, 29783.0, 0.0)
    earth.mass = 5.9726 * 10**24
    earth.r = 6371 * 10**3
    earth.color = (50, 50, 255)
    planets.append(earth)

    mars = Body('Mars', 0.0, 1.52 * globals.AU, 24130.0, 0.0)
    mars.mass = 6.4171 * 10**23
    mars.r = 3389.5 * 10**3
    mars.color = (230, 80, 50)
    planets.append(mars)

    jupiter = Body('Jupiter', 0.0, 5.2 * globals.AU, 13070.0, 0.0)
    jupiter.mass = 1.8986 * 10**27
    jupiter.r = 69911 * 10**3
    jupiter.color = (230, 170, 120)
    planets.append(jupiter)

    saturn = Body('Saturn', 0.0, 9.5 * globals.AU, 9690.0, 0.0)
    saturn.mass = 5.6846 * 10**26
    saturn.r = 58232 * 10**3
    saturn.color = (255, 200, 100)
    planets.append(saturn)

    uran = Body('Uranus', 0.0, 19 * globals.AU, 6810.0, 0.0)
    uran.mass = 8.6832 * 10**25
    uran.r = 25362 * 10**3
    uran.color = (190, 255, 255)
    planets.append(uran)

    neptun = Body('Neptune', 0.0, 30 * globals.AU, 5435.0, 0.0)
    neptun.mass = 1.0243 * 10**26
    neptun.r = 24622 * 10**3
    neptun.color = (80, 160, 255)
    planets.append(neptun)

    pluto = Body('Pluto', 0.0, 45 * globals.AU, 4664.0, 0.0)
    pluto.mass = 1.3033 * 10**22
    pluto.r = 1188.3 * 10**3
    pluto.color = (255, 190, 170)
    planets.append(pluto)

    return planets
