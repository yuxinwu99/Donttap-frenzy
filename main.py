import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time

game = [639, 258, 1262, 879]
window = [639,103, 1264,1039]
previous_clicks = []
max_previous_click_length = 3

def tap(screen):
    global coords, previous_clicks
    clicks = 0
    for y in range(75, len(screen) - 75, 150):
        for x in range(75, len(screen[y]) - 75, 150):
            # print(screen[y][x])
            if screen[y][x] == 0:
                clicks += 1
                actual_x = x + game[0]
                actual_y = y + game[1]
                # print(actual_x,actual_y)
                if [actual_x,actual_y] in previous_clicks:
                    continue
                click(actual_x, actual_y)
                previous_clicks.append([actual_x, actual_y])
                # print(previous_clicks)
                if len(previous_clicks) > max_previous_click_length:
                    del previous_clicks[0]

# only start the program after the mouse is on the left screen
while True:
    mouse_pos = queryMousePosition()
    print(mouse_pos.x,mouse_pos.y)
    if mouse_pos.x <= 0:
        break

start = False
print("alright we good to go")
start_time = time.time()
while True:
    mouse_pos = queryMousePosition()
    current_time = time.time()
    time_spent = current_time - start_time
    print('current time:',time_spent)
    if time_spent > 37:
        break
    if window[0] < mouse_pos.x < window[2] and window[1] < mouse_pos.y < window[3]:

        screen = np.array(ImageGrab.grab(bbox=game))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)

        if start == True:
            tap(screen)
        elif screen[103 - window[1], 639 - window[0]] > 180 and start == False:
            start = True
            click(830,856-100)
            time.sleep(4)
            # cv2.imshow("image", screen)
            # cv2.waitKey(0)
