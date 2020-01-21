# Third party imports
from pynput import keyboard

# Local application imports
from src.main.code.actionMgr import ActionMgr
from src.main.code.windowMgr import WindowMgr

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
    a_mgr = ActionMgr()

    # Main loop
    a_mgr.close_notice_window()
    a_mgr.close_log_in_reward_window()
    a_mgr.close_online_march_window()

    while not end_program:
        # Main decision tree
        a_mgr.lvl_up_quests()
        a_mgr.lvl_up_heroes()
        a_mgr.use_slugs_to_skip_lvls()
        # a_mgr.excavate_slugs()


if __name__ == '__main__':
    main()
