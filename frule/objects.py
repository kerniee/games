from pygame.math import Vector2 as Vector
import globals
from math import ceil
import pygame as pg
import pygame.gfxdraw

globals.init()


class Body:
    def __init__(self, name=None,
                 pos=Vector(0, 0), pos_y=None,
                 speed=Vector(0, 0), speed_y=None,
                 mass=1, r=1, color=0,
                 ):
        self.name = name
        if not (pos_y is None) and (not isinstance(pos, Vector)):
            self.pos = Vector(pos, pos_y)
        else:
            self.pos = pos

        if not (speed_y is None) and (not isinstance(speed, Vector)):
            self.speed = Vector(speed, speed_y)
        else:
            self.speed = speed

        self.mass = mass
        self.r = r
        self.color = color

        self.acc = Vector(0, 0)
        self.surface = None
        # self.force = 0

    def move(self, time):
        self.speed += self.acc * time
        self.pos += (self.speed * time) + ((self.acc * (time ** 2)) / 2)

    def in_outer_space(self):
        if max(self.pos) > globals.AU * 100:
            return True
        else:
            return False

    def apply_force(self, other):
        d = self.pos.distance_to(other.pos)
        if d == self.r + other.r:
            self.acc = Vector(0, 0)
            other.acc = Vector(0, 0)
            return other
        if d < self.r + other.r:
            d = self.r + other.r
        force_num = globals.G * (self.mass * other.mass) / (d ** 2)
        force = other.pos.normalize() * force_num
        self.acc += force / self.mass
        other.acc += force / (other.mass * -1)
        return other

    def get_scaled_pos(self):
        # print(globals.SCALE)
        width, height = globals.SIZE
        scr_pos = self.pos / globals.SCALE
        scr_pos = Vector(scr_pos.x + width // 2, scr_pos.y + height // 2)
        return Vector(ceil(scr_pos.x), ceil(scr_pos.y))
        # return Vector(width//2, height//2)

    def get_scaled_radius(self):
        res = ceil(self.r / globals.SCALE)
        # print(res)
        if res < 0:
            raise ValueError(f'{res:.2e} less then 0')
        else:
            if res > max(globals.SIZE):
                res = max(globals.SIZE)
            # print(res)
            return res

    def draw(self, draw_name=True):
        self.scaled_pos = self.get_scaled_pos()

        self.scaled_r = int(self.get_scaled_radius())
        if abs(self.scaled_pos.x) + self.scaled_r + 1 > globals.SIZE[0] or \
                abs(self.scaled_pos.y) + self.scaled_r + 1 > globals.SIZE[1]:
            return
        if self.scaled_r == 1:
            pg.draw.aaline(self.surface, self.color,
                           [int(x) for x in self.scaled_pos],
                           [int(x) for x in self.scaled_pos], )
        else:
            pg.gfxdraw.filled_circle(self.surface, int(self.scaled_pos.x), int(self.scaled_pos.y), self.scaled_r,
                                     self.color)
            pg.gfxdraw.aacircle(self.surface, int(self.scaled_pos.x), int(self.scaled_pos.y), self.scaled_r,
                                self.color)
            pg.gfxdraw.aacircle(self.surface, int(self.scaled_pos.x), int(self.scaled_pos.y), self.scaled_r-1,
                                self.color)
            temp = pygame.Surface((self.scaled_r*2, self.scaled_r*2), pg.SRCALPHA)
            self.surface.blit(temp, self.scaled_pos, None, pg.BLEND_ADD)

        if draw_name:
            font = pygame.font.Font(None, 16)
            text = font.render(self.name, 1, (255, 255, 255), (0, 0, 0, 0))
            self.surface.blit(text, self.scaled_pos+Vector(3+self.scaled_r, -(3+self.scaled_r)),
                              None, pg.BLEND_ADD)



