from pico2d import *

open_canvas()

character = load_image('Drill04-sheet.png')

# fill here
frame = 0
스
for x in range(0,800,10):
    clear_canvas()

    character.clip_draw(frame*100,0,100,100,800,90)
    update_canvas()
    frame = (frame + 1)%8
    delay(0.05)

close_canvas()
