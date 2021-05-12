import time
import config as cfg
from functions import cal_astral


if __name__ == '__main__':

    while True:

        constell_dict = cal_astral()

        print(constell_dict)

        time.sleep(cfg.SLEEP_TIME)
