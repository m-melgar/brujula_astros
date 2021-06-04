import time

from astropy.coordinates import get_body
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_constellation
from astropy.time import Time

import config as cfg


def cal_astral():
    """
    gets all planets, moon and sun position in sky
    :return: dictionary containing a planet and its constellation position
    """

    solar_system_ephemeris.set('de432s')
    loc = EarthLocation.from_geodetic(lon=cfg.LONGITUDE, lat=cfg.LATITUDE)
    t = Time.now()

    moon_constell = get_constellation(get_body('moon', t, loc))
    mercury_constell = get_constellation(get_body('mercury', t, loc))
    venus_constell = get_constellation(get_body('venus', t, loc))
    mars_constell = get_constellation(get_body('mars', t, loc))
    jupiter_constell = get_constellation(get_body('jupiter', t, loc))
    saturn_constell = get_constellation(get_body('saturn', t, loc))
    uranus_constell = get_constellation(get_body('uranus', t, loc))
    neptune_constell = get_constellation(get_body('neptune', t, loc))
    pluto_constell = get_constellation(get_body('pluto', t, loc))
    sun_constell = get_constellation(get_body('sun', t, loc))


    return {'sun': sun_constell, 'moon': moon_constell, 'mercury': mercury_constell, 'venus': venus_constell,
            'mars': mars_constell, 'jupiter': jupiter_constell, 'saturn': saturn_constell, 'uranus': uranus_constell,
            'neptune': neptune_constell, 'pluto': pluto_constell}


def validate_constell(constell: str):
    """
    Check if constell is form zodiac list in config file (ZODIAC_LIST)
    :param constell: (string) constellation name
    :return: constellation name if valid, None otherwise
    """
    if constell not in cfg.ZODIAC_LIST:
        return None
    else:
        return constell


def set_data_flux(constell_str: str):
    """
    given a constellation returns the data flux array 4 led

    :param constell_str: (str) planet constellation location
    :return: array of 0's and 1's to trigger constellation leds
    """

    LED_BIT_ARRAY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if constell_str == 'Aquarius':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Aquarius')] = 1
    elif constell_str == 'Aries':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Aries')] = 1
    elif constell_str == 'Cancer':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Cancer')] = 1
    elif constell_str == 'Capricornus':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Capricornus')] = 1
    elif constell_str == 'Gemini':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Gemini')] = 1
    elif constell_str == 'Leo':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Leo')] = 1
    elif constell_str == 'Libra':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Libra')] = 1
    elif constell_str == 'Pisces':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Pisces')] = 1
    elif constell_str == 'Sagittarius':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Sagittarius')] = 1
    elif constell_str == 'Scorpius':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Scorpius')] = 1
    elif constell_str == 'Taurus':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Taurus')] = 1
    elif constell_str == 'Virgo':
        LED_BIT_ARRAY[cfg.ZODIAC_LIST.index('Virgo')] = 1
    else:
        pass

    return LED_BIT_ARRAY

def set_data_flux_inverted(constell_str: list):
    """
    given a planet returns the data flux array 4 led

    :param constell_str: (str) planet constellation location
    :return: array of 0's and 1's to trigger constellation leds
    """

    LED_BIT_ARRAY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'sun' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('sun')] = 1
    if 'moon' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('moon')] = 1
    if 'mercury' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('mercury')] = 1
    if 'venus' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('venus')] = 1
    if 'mars' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('mars')] = 1
    if 'jupiter' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('jupiter')] = 1
    if 'saturn' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('saturn')] = 1
    if 'uranus' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('uranus')] = 1
    if 'neptune' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('neptune')] = 1
    if 'pluto' in constell_str:
        LED_BIT_ARRAY[cfg.PLANET_LIST.index('pluto')] = 1

    return LED_BIT_ARRAY


def led_trigger(constell_dic):
    # data flux for moon
    MOON_LED_BITS =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    MERCURY_LED_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    VENUS_LED_BITS =   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    MARS_LED_BITS =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    JUPITER_LED_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    SATURN_LED_BITS =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    URANUS_LED_BITS =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    NEPTUNE_LED_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    PLUTO_LED_BITS =   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    SUN_LED_BITS =     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if validate_constell(constell_dic['moon']):
        MOON_LED_BITS = set_data_flux(constell_dic['moon'])
    if validate_constell(constell_dic['mercury']):
        MERCURY_LED_BITS = set_data_flux(constell_dic['mercury'])
    if validate_constell(constell_dic['venus']):
        VENUS_LED_BITS = set_data_flux(constell_dic['venus'])
    if validate_constell(constell_dic['mars']):
        MARS_LED_BITS = set_data_flux(constell_dic['mars'])
    if validate_constell(constell_dic['jupiter']):
        JUPITER_LED_BITS = set_data_flux(constell_dic['jupiter'])
    if validate_constell(constell_dic['saturn']):
        SATURN_LED_BITS = set_data_flux(constell_dic['saturn'])
    if validate_constell(constell_dic['uranus']):
        URANUS_LED_BITS = set_data_flux(constell_dic['uranus'])
    if validate_constell(constell_dic['neptune']):
        NEPTUNE_LED_BITS = set_data_flux(constell_dic['neptune'])
    if validate_constell(constell_dic['pluto']):
        PLUTO_LED_BITS = set_data_flux(constell_dic['pluto'])
    if validate_constell(constell_dic['sun']):
        SUN_LED_BITS = set_data_flux(constell_dic['sun'])

    return {'moon_bites': listToString(MOON_LED_BITS), 'mercury_bites': listToString(MERCURY_LED_BITS), 'venus_bites': listToString(VENUS_LED_BITS),
            'mars_bites': listToString(MARS_LED_BITS), 'jupyter_bites': listToString(JUPITER_LED_BITS), 'saturn_bites': listToString(SATURN_LED_BITS),
            'uranus_bites': listToString(URANUS_LED_BITS), 'neptune_bites': listToString(NEPTUNE_LED_BITS), 'pluto_bites': listToString(PLUTO_LED_BITS),
            'sun_bites': listToString(SUN_LED_BITS)}


def led_trigger_inverted(constell_dic):

    AQUARIUS_LED_BITS =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ARIES_LED_BITS =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    CANCER_LED_BITS =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    CAPRICORNUS_LED_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    GEMINI_LED_BITS =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    LEO_LED_BITS =         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    LIBRA_LED_BITS =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    PISCES_LED_BITS =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    SAGITTARIUS_LED_BITS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    SCORPIUS_LED_BITS =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    TAURUS_LED_BITS =      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    VIRGO_LED_BITS =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if 'Aquarius' in constell_dic:
        AQUARIUS_LED_BITS = set_data_flux_inverted(constell_dic['Aquarius'])
    if 'Aries' in constell_dic:
        ARIES_LED_BITS = set_data_flux_inverted(constell_dic['Aries'])
    if 'Cancer' in constell_dic:
        CANCER_LED_BITS = set_data_flux_inverted(constell_dic['Cancer'])
    if 'Capricornus' in constell_dic:
        CAPRICORNUS_LED_BITS = set_data_flux_inverted(constell_dic['Capricornus'])
    if 'Gemini' in constell_dic:
        GEMINI_LED_BITS = set_data_flux_inverted(constell_dic['Gemini'])
    if 'Leo' in constell_dic:
        LEO_LED_BITS = set_data_flux_inverted(constell_dic['Leo'])
    if 'Libra' in constell_dic:
        LIBRA_LED_BITS = set_data_flux_inverted(constell_dic['Libra'])
    if 'Pisces' in constell_dic:
        PISCES_LED_BITS = set_data_flux_inverted(constell_dic['Pisces'])
    if 'Sagittarius' in constell_dic:
        SAGITTARIUS_LED_BITS = set_data_flux_inverted(constell_dic['Sagittarius'])
    if 'Scorpius' in constell_dic:
        SCORPIUS_LED_BITS = set_data_flux_inverted(constell_dic['Scorpius'])
    if 'Taurus' in constell_dic:
        TAURUS_LED_BITS = set_data_flux_inverted(constell_dic['Taurus'])
    if 'Virgo' in constell_dic:
        VIRGO_LED_BITS = set_data_flux_inverted(constell_dic['Virgo'])

    return {'aquarius_bites': listToString(AQUARIUS_LED_BITS), 'aries_bites': listToString(ARIES_LED_BITS),
            'cancer_bites': listToString(CANCER_LED_BITS),
            'capricornus_bites': listToString(CAPRICORNUS_LED_BITS), 'gemini_bites': listToString(GEMINI_LED_BITS),
            'leo_bites': listToString(LEO_LED_BITS),
            'libra_bites': listToString(LIBRA_LED_BITS), 'pisces_bites': listToString(PISCES_LED_BITS),
            'sagittarius_bites': listToString(SAGITTARIUS_LED_BITS),
            'scorpius_bites': listToString(SCORPIUS_LED_BITS),
            'taurus_bites': listToString(TAURUS_LED_BITS),
            'virgo_bites': listToString(VIRGO_LED_BITS)}


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)

    # TODO mirar a ver como leches se saca para el shifter
    return str1


def invert_dictionary_map(my_map):
    inv_map = {}
    for k, v in my_map.items():
        inv_map[v] = inv_map.get(v, []) + [k]

    return inv_map


def data_transform_to_register(mydict: dict):
    """
    transform a dict of 10 bits array to dict for 8 bit shift register
    :return: dict of fixed arrays
    """
    # TODO

    serial_dict = [v for k, v in mydict.items()]

    serial_dict = "".join(serial_dict)

    serial_dict = [serial_dict[i:i+8] for i in range(0, len(serial_dict), 8)]

    return serial_dict


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def pretty_transition():

    SERIAL = '0'*120
    for i in range(120):
        SERIAL = replacer(SERIAL, '1', i)
        DATA = [SERIAL[i:i + 8] for i in range(0, len(SERIAL), 8)]

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

        time.sleep(10)

    SERIAL = '1' * 120
    for i in range(120):
        SERIAL = replacer(SERIAL, '0', i)
        DATA = [SERIAL[i:i + 8] for i in range(0, len(SERIAL), 8)]

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

        time.sleep(10)
