"""Reader for grib files.

If indeed there is only one kind of grib file, this one reads it and
creates an object which respects the weather model interface.
"""


import pygrib


class GribModel:
    """
    Grib weather model.
    Implements point_dry_delay and point_hydrostatic_delay.
    """
    def __init__(self):
        raise NotImplemented

    def point_dry_delay(x, y, z):
        """
        Calculate dry delay at a single geocentric point.
        Internally, this interpolates the grib data before performing
        the calculation.
        """
        pass

    def point_hydrostatic_delay(x, y, z):
        """
        Calculate hydrostatic delay at a single geocentric point.
        """
        pass


def load(filename):
    #with pygrib.open(filename, 'r') as f:
    pass
 

def fetch():
    pass
