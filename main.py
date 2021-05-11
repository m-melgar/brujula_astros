import time
import skyfield
import config as cfg
from skyfield.api import N, W, load, wgs84
from functions import cal_astral
import astropy
from astropy import coordinates
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body, get_moon



if __name__ == '__main__':
    # planets_main = load('de440s.bsp')
    # astral_dict = cal_astral(planets_main)
    # load time

    ts = load.timescale()
    t = ts.now()

    planets_main = load('de421.bsp')
    astral_dict = cal_astral(planets_main)
    earth = planets_main['earth']
    earth_city = earth + wgs84.latlon(cfg.NORTH * N, cfg.WEST * W, elevation_m=cfg.ELEVATION)
    print(astral_dict["moon"].position.to(earth_city))


    t = Time.now()

    #astropy.coordinates.get_constellation()


    loc = EarthLocation.of_address('madrid')
    print(loc)
    print(get_moon(t, loc) )