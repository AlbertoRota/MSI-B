# Standard library imports
import random
from time import sleep

# Third party imports
import pyautogui

# Local application imports
import src.main.code.coordinates as coords
from src.main.code.imageMatcher import ImageMatcher
from src.main.code.windowMgr import WindowMgr


class ActionMgr:
    """Encapsulates the steps required to perform high level actions"""

    def __init__(self):
        """Constructor"""
        self._im = ImageMatcher()
        self._w_mgr = WindowMgr()

        self._slot_areas = [coords.hero_slot_1, coords.hero_slot_2, coords.hero_slot_3, coords.hero_slot_4, coords.hero_slot_5, coords.hero_slot_6]
        self._unlock_up_quests_areas = [coords.quest_slot_5, coords.quest_slot_4]
        self._lvl_up_quests_areas = [coords.quest_slot_3, coords.quest_slot_2, coords.quest_slot_1]

    def close_notice_window(self):
        if self._im.is_notice_caption(self._w_mgr.capture_game_area(coords.notice_caption)):
            self._click_in_area(coords.notice_close, 0.5, 1)

    def close_log_in_reward_window(self):
        if self._im.is_log_in_reward_caption(self._w_mgr.capture_game_area(coords.log_in_reward_caption)):
            self._click_in_area(coords.log_in_reward_close, 1, 1.5)
            self._click_in_area(coords.log_in_reward_close, 1, 1.5)

    def close_online_march_window(self):
        if self._im.is_offline_march_caption(self._w_mgr.capture_game_area(coords.offline_march_caption)):
            self._click_in_area(coords.offline_march_close, 0.5, 1)

    def lvl_up_heroes(self):
        random.shuffle(self._slot_areas)
        for hero_slot_area in self._slot_areas:
            self._hold_in_area(hero_slot_area, 1, 3)

    def use_slugs_to_skip_lvls(self):
        self._click_in_area(coords.slot_switch_slug)
        sleep(2)
        random.shuffle(self._slot_areas)
        for slug_slot_area in self._slot_areas:
            self._click_in_area(slug_slot_area, 0.2, 1)
        sleep(2)
        self._click_in_area(coords.slot_switch_slug)

    def lvl_up_quests(self):
        self._click_in_area(coords.open_quest_button, 2.0, 3.5)
        for unlock_quest_slot_area in self._unlock_up_quests_areas:
            self._click_in_area(unlock_quest_slot_area, 0.5, 1)
        for lvl_up_quest_slot_area in self._lvl_up_quests_areas:
            self._hold_in_area(lvl_up_quest_slot_area, 1, 3)
        self._click_in_area(coords.close_quest_button, 0.5, 1.5)

    def excavate_slugs(self):
        # Open correct menu
        self._click_in_area(coords.open_slug_button, 2.0, 3.5)
        self._click_in_area(coords.open_excavation_site_button, 2.0, 3.5)

        # Excavate Expert slugs
        if not self._im.is_expert_excavation_exhausted(self._w_mgr.capture_game_area(coords.expert_excavation_exhausted)):
            self._click_in_area(coords.expert_excavation_button)
            while not self._im.is_excavation_result_close(self._w_mgr.capture_game_area(coords.close_excavation_result)):
                sleep(1)
            self._click_in_area(coords.close_excavation_result, 2.0, 3.5)

        # Excavate Advanced slugs
        if not self._im.is_advanced_excavation_exhausted(self._w_mgr.capture_game_area(coords.advanced_excavation_exhausted)):
            self._click_in_area(coords.advanced_excavation_button)
            while not self._im.is_excavation_result_close(
                    self._w_mgr.capture_game_area(coords.close_excavation_result)):
                sleep(1)
            self._click_in_area(coords.close_excavation_result, 2.0, 3.5)

        # Excavate General slugs
        if not self._im.is_general_excavation_exhausted(self._w_mgr.capture_game_area(coords.general_excavation_exhausted)):
            self._click_in_area(coords.general_excavation_button)
            while not self._im.is_excavation_result_close(
                    self._w_mgr.capture_game_area(coords.close_excavation_result)):
                sleep(1)
            self._click_in_area(coords.close_excavation_result, 2.0, 3.5)

        # Close all menus
        self._click_in_area(coords.close_excavation_result, 2.0, 3.5)

    def _click_in_area(self, area, min_time=1.0, max_time=1.0):
        pyautogui.click(
            random.randrange(coords.game_area[0] + area[0], coords.game_area[0] + area[2]),
            random.randrange(coords.game_area[1] + area[1], coords.game_area[1] + area[3])
        )
        if min_time != 0 and max_time != 0:
            sleep(random.uniform(min_time, max_time))

    def _hold_in_area(self, area, min_time, max_time):
        pyautogui.moveTo(
            random.randrange(coords.game_area[0] + area[0], coords.game_area[0] + area[2]),
            random.randrange(coords.game_area[1] + area[1], coords.game_area[1] + area[3])
        )
        pyautogui.mouseDown()
        sleep(random.uniform(min_time, max_time))
        pyautogui.mouseUp()