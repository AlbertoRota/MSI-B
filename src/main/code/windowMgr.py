# Third party imports
import numpy as np
import cv2
import win32gui, win32com.client
from PIL import ImageGrab

# Local application imports
import src.main.code.coordinates as coords


def _img_2_np(image):
    # Convert it to NumPy
    image_np = np.array(
        image.getdata(),
        dtype='uint8'
    ).reshape((
        image.size[1],
        image.size[0],
        3
    ))

    # Convert it to "RGB"
    return cv2.cvtColor(
        image_np,
        cv2.COLOR_BGR2RGB
    )


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = win32gui.FindWindow(None, r'BlueStacks')

    def reposition_window(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._handle)
        win32gui.MoveWindow(
            self._handle,
            coords.window_area[0],
            coords.window_area[1],
            coords.window_area[2],
            coords.window_area[3],
            True
        )

    def capture_full_screen(self):
        return ImageGrab.grab()

    def capture_full_window(self):
        return ImageGrab.grab(coords.window_area)

    def capture_full_game_area(self):
        return ImageGrab.grab(coords.game_area)

    def capture_game_area(self, area):
        screen_coords = (
            coords.game_area[0] + area[0],
            coords.game_area[1] + area[1],
            coords.game_area[0] + area[2],
            coords.game_area[1] + area[3]
        )
        return _img_2_np(ImageGrab.grab(screen_coords))
