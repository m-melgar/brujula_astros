import time
import config as cfg
import functions
from functions import cal_astral, led_trigger, led_trigger_inverted
from shifter import Shifter


if __name__ == '__main__':

    s1  = Shifter(cfg.SR_1_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s2  = Shifter(cfg.SR_2_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s3  = Shifter(cfg.SR_3_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s4  = Shifter(cfg.SR_4_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s5  = Shifter(cfg.SR_5_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s6  = Shifter(cfg.SR_6_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s7  = Shifter(cfg.SR_7_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s8  = Shifter(cfg.SR_8_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s9  = Shifter(cfg.SR_9_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s10 = Shifter(cfg.SR_10_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s11 = Shifter(cfg.SR_11_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s12 = Shifter(cfg.SR_12_INPUT, cfg.CLOCK_PIN, cfg.CLEAR_PIN)

    s1.setupBoard()
    s2.setupBoard()
    s3.setupBoard()
    s4.setupBoard()
    s5.setupBoard()
    s6.setupBoard()
    s7.setupBoard()
    s8.setupBoard()
    s9.setupBoard()
    s10.setupBoard()
    s11.setupBoard()
    s2.setupBoard()

    while True:

        constell_dict_ = cal_astral()
        constell_dict_inverted = functions.invert_dictionary_map(constell_dict_)
        DATA = functions.data_transform_to_register(led_trigger_inverted(constell_dict_inverted))

        if cfg.DEBUG:

            print(led_trigger(constell_dict_))
            print('---'*20)
            print(constell_dict_)
            print('---' * 20)
            print(constell_dict_inverted)
            print('---' * 20)
            print(led_trigger_inverted(constell_dict_inverted))

            AA = functions.data_transform_to_register(led_trigger_inverted(constell_dict_inverted))
            print(AA)

        s1.setValue(DATA[0])
        s2.setValue(DATA[1])
        s3.setValue(DATA[2])
        s4.setValue(DATA[3])
        s5.setValue(DATA[4])
        s6.setValue(DATA[5])
        s7.setValue(DATA[6])
        s8.setValue(DATA[7])
        s9.setValue(DATA[8])
        s10.setValue(DATA[9])
        s11.setValue(DATA[10])
        s12.setValue(DATA[11])

        time.sleep(cfg.SLEEP_TIME)

        # TODO si cambian las cosntelaciones hacer transición bonita


