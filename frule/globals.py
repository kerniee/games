def init():
    global G, SIZE, AU, SCALE, SCROLL_SCALE, TIMESTEP, FPS
    G = 6.6743 * pow(10, -11)
    SIZE = (1200, 900)
    AU = 149597870700
    SCALE = AU * 0.01
    SCROLL_SCALE = 2
    TIMESTEP = 1
    FPS = 30
