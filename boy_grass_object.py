from pyclbr import Class

from pico2d import *
import random


# Game object class here
class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 0
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(2,8)
        self.sizeX = self.sizeY = random.randint(20,100)
        self.dt = 0

    def update(self):
        self.dt += 1

        if self.y < 600 - self.sizeY // 2:
            self.y += self.speed
        else:
            self.y += math.sin(self.dt) * self.speed
        
    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y, self.sizeX, self.sizeY)

    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        if self.x > 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global world

    world = []
    running = True
    grass = Grass()
    world.append(grass)
    ball = [Ball() for i in range(20)]
    world += ball

    team = [Boy() for i in range(11)]
    world += team

def update_world():
    for o in world:
      o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
clear_canvas()
