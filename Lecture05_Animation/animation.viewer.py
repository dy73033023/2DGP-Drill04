from pico2d import *

open_canvas()

character = load_image('Drill04-sheet.png')

# fill here

sheet_y = 56

def roll():
    frame = 0
    for x in range(0,400,10):
        clear_canvas()
        character.clip_draw(frame * 100, 0, 48, sheet_y, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 9
        delay(0.05)

def walk():
    pass

def run():
    pass


def stand():
    pass

while(1):
    roll()

close_canvas()
