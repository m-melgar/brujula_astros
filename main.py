import time
import config as cfg
from functions import cal_astral,led_trigger


if __name__ == '__main__':

    while True:

        constell_dict_ = cal_astral()

        print(led_trigger(constell_dict_))
        print('---'*20)
        print(constell_dict_)

        time.sleep(cfg.SLEEP_TIME)
