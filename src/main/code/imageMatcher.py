# Third party imports
import cv2 as cv


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self):
        """Constructor"""
        self._threshold = 0.1
        self._notice_caption = cv.imread('src/main/resources/templates/Notice_Caption.png', cv.IMREAD_COLOR)
        self._offline_march_caption = cv.imread('src/main/resources/templates/OfflineMarch_Caption.png', cv.IMREAD_COLOR)

    def is_notice_caption(self, image):
        """Returns True if the image contains the "Notice" caption, False otherwise."""
        return self._match(image, self._notice_caption)

    def is_offline_march_caption(self, image):
        """Returns True if the image contains the "Offline-March" caption, False otherwise."""
        return self._match(image, self._offline_march_caption)

    def _match(self, image, template):
        """Returns True if the image contains the template, False otherwise."""
        return cv.matchTemplate(
            image,
            template,
            cv.TM_SQDIFF,
            mask=None
        ).min() < self._threshold
