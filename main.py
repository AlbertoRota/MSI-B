# Standard library imports
import random
from time import sleep

# Third party imports
import pyautogui
from pynput import keyboard

# Local application imports
import src.main.code.coordinates as coords
from src.main.code.windowMgr import WindowMgr
from src.main.code.imageMatcher import ImageMatcher

# Global variables
end_program = False


def on_press(key):
    global end_program

    if key == keyboard.Key.shift_r:
        end_program = True  # Flip global flag
        return False  # Stop listener


def main():
    # Variable declaration and initialization
    global end_program

    # Initialize keyboard listener on a separate thread
    keyboard.Listener(on_press=on_press).start()

    # Initialize all the internal modules.
    w_mgr = WindowMgr()
    w_mgr.reposition_window()

    im = ImageMatcher()

    # Main loop
    while not end_program:
        # Main decision tree
        if im.is_offline_march_caption(w_mgr.capture_game_area(coords.offline_march_caption)):
            click_in_area(coords.offline_march_close)
        else:
            click_in_area(coords.slot_switch_slug)
            slot_areas = [coords.hero_slot_1, coords.hero_slot_2, coords.hero_slot_3, coords.hero_slot_4]
            random.shuffle(slot_areas)
            for slot_area in slot_areas:
                click_in_area(slot_area, 1, 3)


def click_in_area(area, min_time=0, max_time=0):
    pyautogui.click(
        random.randrange(coords.game_area[0] + area[0], coords.game_area[0] + area[2]),
        random.randrange(coords.game_area[1] + area[1], coords.game_area[1] + area[3])
    )
    if min_time != 0 and max_time != 0:
        sleep(random.randrange(min_time, max_time))


def hold_in_area(area, min_time, max_time):
    pyautogui.moveTo(
        random.randrange(coords.game_area[0] + area[0], coords.game_area[0] + area[2]),
        random.randrange(coords.game_area[1] + area[1], coords.game_area[1] + area[3])
    )
    pyautogui.mouseDown()
    sleep(random.randrange(min_time, max_time))
    pyautogui.mouseUp()


if __name__ == '__main__':
    main()
