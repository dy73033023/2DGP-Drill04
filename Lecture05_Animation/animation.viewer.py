from pico2d import *

open_canvas()

character = load_image('Drill04-sheet.png')

# fill here
sheet_x = 44
sheet_y = 56

def roll():
    frame = 0
    for x in range(0, 800, 7):
        clear_canvas()
        character.clip_draw(frame * 100, 0, sheet_x, sheet_y, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.05)

def walk():
    pass

def run():
    pass


def stand():
    pass

rolling()

close_canvas()
