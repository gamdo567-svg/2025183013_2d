from pyclbr import Class

from pico2d import *
import random


# Game object class here
class Zombie:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 150
        self.image = load_image('zombie_run_animation.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 5
        if self.x < 0:
            self.x = 800
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        scale = 0.4

        self.image.clip_composite_draw(
            self.frame * frame_width, 0,
            frame_width, frame_height,
            0, 'h',                
            self.x, self.y,
            int(frame_width * scale),
            int(frame_height * scale)
        )
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
    team = [Boy() for i in range(11)]
    world += team
    zombie_team = [Zombie() for i in range(5)]
    world += zombie_team

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
