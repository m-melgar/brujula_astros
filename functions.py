from skyfield.api import Loader
from skyfield.api import N, W, load, wgs84
import config as cfg

def install():
    load = Loader('~/skyfield-data',verbose=True)


def cal_astral(planets):
    """

    :return: dictionary containing astral positions
    """

    ts = load.timescale()
    t = ts.now()

    moon, mercury, venus,earth, mars, jupiter, saturn, uranus, neptune, pluto = planets['moon'], planets['mars'], planets['venus'], planets['earth'], planets['mars'], planets[5], planets[6], planets[7], planets[8], planets[9]

    earth_city = earth + wgs84.latlon(cfg.NORTH * N, cfg.WEST * W, elevation_m=cfg.ELEVATION)

    astrometric = earth_city.at(t).observe(mars)

    return {'moon': earth_city.at(t).observe(moon), 'mercury': earth_city.at(t).observe(mercury).position.au, 'venus': earth_city.at(t).observe(venus).position.au, 'mars':earth_city.at(t).observe(mars).position.au, 'jupiter':earth_city.at(t).observe(jupiter).position.au, 'saturn': earth_city.at(t).observe(saturn).position.au, 'uranus': earth_city.at(t).observe(uranus).position.au, 'neptune':earth_city.at(t).observe(neptune).position.au, 'pluto':earth_city.at(t).observe(pluto).position.au}


def get_constellation(astra_dict):
    """

    :param astra_dict: dictionary with astral positions
    :return: dictionary
    """