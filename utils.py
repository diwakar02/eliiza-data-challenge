from shapely.geometry import Polygon, mapping
from collections.abc import Iterable
import shapely.wkt


# ----private------#
def _flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from _flatten(el)
        else:
            yield el


def _set_precision(coords, precision):
    result = []
    try:
        return round(coords, int(precision))
    except TypeError:
        for coord in coords:
            result.append(_set_precision(coord, precision))
    return result


# ----public-------#
def to_poly(raw_data):
    it = iter(list(_flatten(raw_data)))
    return list(zip(it, it))


def to_multi_poly(raw_data):
    return [[[tuple(item) for item in sub] 
            for sub in second_list] for second_list in raw_data]


def poly_in_poly(poly1, poly2):
    p1 = Polygon(poly1)
    p2 = Polygon(poly2)
    return p2.contains(p1)


def set_precision(coords, precision):
    result = []
    try:
        return round(coords, int(precision))
    except TypeError:
        for coord in coords:
            result.append(_set_precision(coord, precision))
    return result


def cleaned_polygon(row):
    filterexp = row.replace("POLYGON ", '') 
    cleanedRow = ', '.join(' '.join(s) for s in zip(*[iter(filterexp.split())]*2)) 
    cleanedRow = "POLYGON " + cleanedRow
    poly = shapely.wkt.loads(cleanedRow)
    geo_poly = mapping(poly)
    return geo_poly['coordinates']