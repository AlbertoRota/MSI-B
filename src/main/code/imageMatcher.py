# Third party imports
import cv2 as cv

# Local application imports
import src.main.code.coordinates as coords
from src.main.code.windowMgr import WindowMgr


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self):
        """Constructor"""
        self._threshold = 0.1
        self._w_mgr = WindowMgr()

        path = 'src/main/resources/templates/'
        self._notice_caption = cv.imread(path + 'Notice_Caption.png', cv.IMREAD_COLOR)
        self._log_in_reward_caption = cv.imread(path + 'LogInReward_Caption.png', cv.IMREAD_COLOR)
        self._offline_march_caption = cv.imread(path + 'OfflineMarch_Caption.png', cv.IMREAD_COLOR)
        self._expert_excavation_exhausted = cv.imread(path + 'Excavation_ExpertExhausted.png', cv.IMREAD_COLOR)
        self._advanced_excavation_exhausted = cv.imread(path + 'Excavation_AdvancedExhausted.png', cv.IMREAD_COLOR)
        self._general_excavation_exhausted = cv.imread(path + 'Excavation_GeneralExhausted.png', cv.IMREAD_COLOR)
        self._excavation_result_close = cv.imread(path + 'ExcavationResult_close.png', cv.IMREAD_COLOR)
        self._batch_promote_error = cv.imread(path + 'BatchPromote_Error.png', cv.IMREAD_COLOR)

    def is_notice_caption(self):
        """Returns True if the image contains the "Notice" caption, False otherwise."""
        image = self._w_mgr.capture_game_area(coords.notice_caption)
        return self._match(image, self._notice_caption)

    def is_log_in_reward_caption(self):
        """Returns True if the image contains the "Log in rewards" caption, False otherwise."""
        image = self._w_mgr.capture_game_area(coords.log_in_reward_caption)
        return self._match(image, self._log_in_reward_caption)

    def is_offline_march_caption(self):
        """Returns True if the image contains the "Offline-March" caption, False otherwise."""
        image = self._w_mgr.capture_game_area(coords.offline_march_caption)
        return self._match(image, self._offline_march_caption)

    def is_expert_excavation_exhausted(self):
        return self._fuzzy_match(coords.expert_excavation_exhausted, self._expert_excavation_exhausted)

    def is_advanced_excavation_exhausted(self):
        return self._fuzzy_match(coords.advanced_excavation_exhausted, self._advanced_excavation_exhausted)

    def is_general_excavation_exhausted(self):
        return self._fuzzy_match(coords.general_excavation_exhausted, self._general_excavation_exhausted)

    def is_excavation_result_close(self):
        """Returns True if the image contains the "Excavation result" close, False otherwise."""
        image = self._w_mgr.capture_game_area(coords.close_excavation_result)
        return self._match(image, self._excavation_result_close)

    def is_batch_promote_error(self):
        """Returns True if the image contains the "Excavation result" close, False otherwise."""
        image = self._w_mgr.capture_game_area(coords.batch_promote_slugs_error)
        return self._match(image, self._batch_promote_error)

    def _match(self, image, template):
        """Returns True if the image contains the template, False otherwise."""
        return cv.matchTemplate(
            image,
            template,
            cv.TM_SQDIFF,
            mask=None
        ).min() < self._threshold

    def _fuzzy_match(self, poi, template):
        """Returns True if the image contains the template, False otherwise."""
        image = self._w_mgr.capture_game_area((
            poi[0] - 10,
            poi[1] - 10,
            poi[2] + 10,
            poi[3] + 10,
        ))
        return cv.matchTemplate(
            image,
            template,
            cv.TM_SQDIFF,
            mask=None
        ).min() < 10
