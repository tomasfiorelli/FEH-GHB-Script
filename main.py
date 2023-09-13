import os
import pandas as pd
import pyautogui as auto
from time import time, sleep

# List of images to find on screen and screen area
images = ['lunatic', 'fight', 'skip', 'auto-battle-1', 'auto-battle-2', 'stage-clear']
right_screen = (960, 0, 960, 1080)

# FUNCTIONS

def get_coordinates(image, screen):
    while True:
        screenshot = auto.screenshot(region=screen)
        button = auto.locate(image, screenshot, grayscale=True, confidence=.95)
        if button != None:
            x, y = auto.center(button)
            coords = (int(x) + screen[0], int(y))
            return coords

def click(button_coordinates):
    auto.moveTo(button_coordinates[0], button_coordinates[1])
    sleep(1)
    auto.leftClick(button_coordinates[0], button_coordinates[1])


# MAIN LOOP

flag = False
current_step = 0
loop_time = time()

while(True):
    if current_step == 0:
        df = pd.read_csv('heroes.csv')
        print(df, '\n')
        if flag:
            exit()
        sleep(2.5)

    print(f'Searching image [STEP: {images[current_step]}]', end=' ')
    coordinates = get_coordinates(f'images\\{images[current_step]}.png', right_screen)
    print(f'Image found at {coordinates}')
    click(coordinates)

    if current_step == 5:
        # HM file controller
        df['HM'] += 5
        for i in range(4):
            if df['HM'][i] > 9000:
                df['HM'][i] = 9000
        if df['HM'].sum() == 4 * 9000:
            flag = True
        df.to_csv('heroes.csv', index=False)
        os.system('cls')

    current_step = (current_step + 1) % 6

    # DEBUG
    loop_time = time()