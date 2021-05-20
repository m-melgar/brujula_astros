from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_constellation
from astropy.coordinates import get_body
import config as cfg
import numpy as np


def cal_astral():
    """
    gets all planets, moon and sun position in sky
    :return: dictionary containing a planet and its constellation position
    """

    solar_system_ephemeris.set('de432s')
    loc = EarthLocation.from_geodetic(lon=cfg.LONGITUDE,lat=cfg.LATITUDE)
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
    sun_constell = get_constellation(get_body('sun',t,loc))

    return {'sun':sun_constell,'moon': moon_constell, 'mercury': mercury_constell, 'venus': venus_constell, 'mars': mars_constell, 'jupiter': jupiter_constell, 'saturn': saturn_constell, 'uranus': uranus_constell, 'neptune': neptune_constell, 'pluto': pluto_constell}


def validate_constell(constell:str):
    """
    Check if constell is form zodiac list in config file (ZODIAC_LIST)
    :param constell: (string) constellation name
    :return: constellation name if valid, None otherwise
    """
    if constell not in cfg.ZODIAC_LIST:
        return None
    else:
        return constell


def set_data_flux(constell_str:str):

    """
    given a constellation returns the data flux array 4 led

    :param constell_str: (str) planet constellation location
    :return: array of 0's and 1's to trigger constellation leds
    """

    LED_BIT_ARRAY = np.array([0,0,0,0,0,0,0,0,0,0,0,0])

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


def led_trigger(constell_dic):


    # data flux for moon
    MOON_LED_BITS =    np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    MERCURY_LED_BITS = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    VENUS_LED_BITS =   np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    MARS_LED_BITS =    np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    JUPITER_LED_BITS = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    SATURN_LED_BITS =  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    URANUS_LED_BITS =  np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    NEPTUNE_LED_BITS = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    PLUTO_LED_BITS =   np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    SUN_LED_BITS =     np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

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

    return MOON_LED_BITS,MERCURY_LED_BITS,VENUS_LED_BITS,MARS_LED_BITS,JUPITER_LED_BITS,SATURN_LED_BITS,URANUS_LED_BITS,NEPTUNE_LED_BITS,PLUTO_LED_BITS,SUN_LED_BITS