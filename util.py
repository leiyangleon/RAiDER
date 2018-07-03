"""Geodesy-related utility functions."""


import numpy
import pyproj


def sind(x):
    """Return the sine of x when x is in degrees."""
    return numpy.sin(numpy.radians(x))


def cosd(x):
    """Return the cosine of x when x is in degrees."""
    return numpy.cos(numpy.radians(x))


def tand(x):
    """Return degree tangent."""
    return numpy.tan(numpy.radians(x))


def lla2ecef(lat, lon, height):
    ecef = pyproj.Proj(proj='geocent')
    lla = pyproj.Proj(proj='latlong')

    return pyproj.transform(lla, ecef, lon, lat, height)


def toXYZ(lats, lons, hts):
    """Convert lat, lon, geopotential height to x, y, z in ECEF."""
    # Convert geopotential to geometric height. This comes straight from
    # TRAIN
    g0 = 9.80665
    # Map of g with latitude (I'm skeptical of this equation)
    g = 9.80616*(1 - 0.002637*cosd(2*lats) + 0.0000059*(cosd(2*lats))**2)
    Rmax = 6378137
    Rmin = 6356752
    Re = numpy.sqrt(1/(((cosd(lats)**2)/Rmax**2) + ((sind(lats)**2)/Rmin**2)))

    # Calculate Geometric Height, h
    h = (hts*Re)/(g/g0*Re - hts)
    return lla2ecef(lats, lons, h)


def big_and(*args):
    result = args[0]
    for a in args[1:]:
        result = numpy.logical_and(result, a)
    return result
