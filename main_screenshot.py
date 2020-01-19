# Standard library imports
import os
import time

# Third party imports
from pynput import keyboard

# Local application imports
import src.main.code.coordinates as coords

from src.main.code.windowMgr import WindowMgr

# Global variables
end_program = False
w_mgr = WindowMgr()


def on_press(key):
    """Pressing "Right Sift" will stop the program, "Tab" will take an snapshot."""
    global end_program, w_mgr
    if key == keyboard.Key.shift_r:
        end_program = True
        return False
    else:
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        if k == "1":
            save_screenshot(w_mgr.capture_full_screen())
        elif k == "2":
            save_screenshot(w_mgr.capture_full_window())
        elif k == "3":
            save_screenshot(w_mgr.capture_full_game_area())
        elif k == "4":
            save_screenshot(w_mgr.capture_game_area_as_img(coords.notice_caption))


def save_screenshot(screenshot):
    """Takes a full-screen snapshot and saves it."""
    img_name = os.getcwd() + '/src/main/resources/window_snap_' + str(int(time.time())) + '.png'
    screenshot.save(img_name, 'PNG')
    print('New screenshot taken: ' + img_name)


def main():
    """Program entry point."""
    global end_program, w_mgr

    w_mgr.reposition_window()
    keyboard.Listener(on_press=on_press).start()
    while not end_program:
        pass


if __name__ == '__main__':
    main()