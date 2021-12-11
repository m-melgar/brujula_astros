import time
import config as cfg
import functions
import RPi.GPIO as gpio
from functions import cal_astral, led_trigger, led_trigger_inverted
from shifter import Shifter

if __name__ == '__main__':

    # SETUP
#    sf = Shifter(cfg.SR_DB_A, cfg.SR_DB_B,cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s1 = Shifter(cfg.SR_1_A, cfg.SR_1_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s2 = Shifter(cfg.SR_2_A, cfg.SR_2_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s3 = Shifter(cfg.SR_3_A, cfg.SR_3_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s4 = Shifter(cfg.SR_4_A, cfg.SR_4_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s5 = Shifter(cfg.SR_5_A, cfg.SR_5_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s6 = Shifter(cfg.SR_6_A, cfg.SR_6_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s7 = Shifter(cfg.SR_7_A, cfg.SR_7_B, cfg.CLOCK_PIN, cfg.CLEAR_PIN)
    s1.setValue(8)
    s2.setValue(8)
    s3.setValue(8)
    s4.setValue(8)
    s5.setValue(8)
    s6.setValue(8)
    s7.setValue(8)
    time.sleep(5)
    s1.clear()
    s2.clear()
    s3.clear()
    s4.clear()
    s5.clear()
    s6.clear()
    s7.clear()
    s1.setValue(0)
    s2.setValue(0)
    s3.setValue(0)
    s4.setValue(0)
    s5.setValue(0)
    s6.setValue(0)
    s7.setValue(0)
    time.sleep(5)
    s1.clear()
    s2.clear()
    s3.clear()
    s4.clear()
    s5.clear()
    s6.clear()
    s7.clear()

    gpio.cleanup()

    """
    # CONSTELLATION
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

        constell_dict_ = cal_astral()
        constell_dict_inverted = functions.invert_dictionary_map(constell_dict_)
        DATA_NEW = functions.data_transform_to_register(led_trigger_inverted(constell_dict_inverted))

        if DATA_NEW != DATA:
            functions.pretty_transition()
    """
   
