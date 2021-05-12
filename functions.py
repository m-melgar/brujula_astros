from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_constellation
from astropy.coordinates import get_body
import config as cfg

def cal_astral():
    """

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

    return {'moon': moon_constell, 'mercury': mercury_constell, 'venus': venus_constell, 'mars': mars_constell, 'jupiter': jupiter_constell, 'saturn': saturn_constell, 'uranus': uranus_constell, 'neptune': neptune_constell, 'pluto': pluto_constell}

