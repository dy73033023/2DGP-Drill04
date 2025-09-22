from pico2d import *

open_canvas()

character = load_image('Drill04-sheet.png')

# fill here

sheet_y = 56

def roll():
    frame = 0
    for x in range(0,400,10):
        clear_canvas()
        character.clip_draw(frame * 49, 0, 49, sheet_y, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

def stand():
    frame = 0
    for x in range(0, 400, 10):
        clear_canvas()
        character.clip_draw(frame * 44+5, sheet_y * 5, 44, sheet_y * 6, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)

def run():
    frame = 0
    for x in range(0, 400, 10):
        clear_canvas()
        character.clip_draw(frame * 72 + 39, sheet_y, 72, sheet_y, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)

def walk():
    frame = 0
    for x in range(0, 400, 10):
        clear_canvas()
        character.clip_draw(frame * 38+8, sheet_y *3, 38, sheet_y, 400, 300, 300, 300)
        update_canvas()
        frame = (frame + 1) % 10
        delay(0.1)

while(1): #무한 반복
    #roll()
    #stand()
    #run()
    walk()
close_canvas()
