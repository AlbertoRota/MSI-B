# Third party imports
import numpy as np
import cv2
import win32gui, win32com.client
from PIL import ImageGrab


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
        self._window_area = (0, 0, 830, 555)
        self._game_area = (7, 47, 825, 507)

    def reposition_window(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._handle)
        win32gui.MoveWindow(self._handle, 0, 0, 830, 555, True)

    def capture_full_screen(self):
        return ImageGrab.grab()

    def capture_full_window(self):
        return ImageGrab.grab(self._window_area)

    def capture_full_game_area(self):
        return ImageGrab.grab(self._game_area)