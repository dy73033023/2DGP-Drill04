from pico2d import *

open_canvas()

character = load_image('Drill04-sheet.png')

# fill here
frame = 0

def walk():
    pass

def run():
    pass

def rolling():
    pass

def stand():
    pass

for x in range(0,800,10):
    clear_canvas()
    character.clip_draw(frame*100,0,44,56,400,300,500,500)
    update_canvas()
    frame = (frame + 1)%9
    delay(0.05)

close_canvas()
