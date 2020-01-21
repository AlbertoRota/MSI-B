# Third party imports
import cv2 as cv


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self):
        """Constructor"""
        self._threshold = 0.1

        path = 'src/main/resources/templates/'
        self._notice_caption = cv.imread(path + 'Notice_Caption.png', cv.IMREAD_COLOR)
        self._log_in_reward_caption = cv.imread(path + 'LogInReward_Caption.png', cv.IMREAD_COLOR)
        self._offline_march_caption = cv.imread(path + 'OfflineMarch_Caption.png', cv.IMREAD_COLOR)
        self._expert_excavation_exhausted = cv.imread(path + 'Excavation_ExpertExhausted.png', cv.IMREAD_COLOR)
        self._advanced_excavation_exhausted = cv.imread(path + 'Excavation_AdvancedExhausted.png', cv.IMREAD_COLOR)
        self._general_excavation_exhausted = cv.imread(path + 'Excavation_GeneralExhausted.png', cv.IMREAD_COLOR)
        self._excavation_result_close = cv.imread(path + 'ExcavationResult_close.png', cv.IMREAD_COLOR)

    def is_notice_caption(self, image):
        """Returns True if the image contains the "Notice" caption, False otherwise."""
        return self._match(image, self._notice_caption)

    def is_log_in_reward_caption(self, image):
        """Returns True if the image contains the "Log in rewards" caption, False otherwise."""
        return self._match(image, self._log_in_reward_caption)

    def is_offline_march_caption(self, image):
        """Returns True if the image contains the "Offline-March" caption, False otherwise."""
        return self._match(image, self._offline_march_caption)

    def is_expert_excavation_exhausted(self, image):
        return self._match(image, self._expert_excavation_exhausted)

    def is_advanced_excavation_exhausted(self, image):
        return self._match(image, self._advanced_excavation_exhausted)

    def is_general_excavation_exhausted(self, image):
        return self._match(image, self._general_excavation_exhausted)

    def is_excavation_result_close(self, image):
        """Returns True if the image contains the "Excavation result" close, False otherwise."""
        return self._match(image, self._excavation_result_close)

    def _match(self, image, template):
        """Returns True if the image contains the template, False otherwise."""
        return cv.matchTemplate(
            image,
            template,
            cv.TM_SQDIFF,
            mask=None
        ).min() < self._threshold
