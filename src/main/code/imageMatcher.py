# Third party imports
import cv2 as cv


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self):
        """Constructor"""
        self._offline_march_caption = cv.imread('src/main/resources/templates/OfflineMarch_Caption.png', cv.IMREAD_COLOR)

    def is_offline_march_caption(self, image, threshold=0.1):
        """Returns True if the image contains the "Offline-March" caption, False otherwise."""
        return cv.matchTemplate(
            image,
            self._offline_march_caption,
            cv.TM_SQDIFF,
            mask=None
        ).min() < threshold

