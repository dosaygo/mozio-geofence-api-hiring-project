import json

from google.appengine.api import search

import convert

"""
  Limitations:

    1. Providers can only enter a single territory whose set of points does not result in a radius larger than 250 m. So providers need to enter their territories in a piecemeal fashion. 

    2. When searching for a latitude and longitude we return all territories whose centre of operations ( as defined by the centroid in the polygon of the territory corners ), is within the maximum radius of a territory. So this means that the territories so returned, are not guaranteed to intersect with the given point, tho they are guaranteed to be within ( or more strictly, to have their centres within ) MAX_TERRITORY_RADIUS of the given point. 
"""

MAX_TERRITORY_RADIUS_M = 250

def compute_centroid( geopt_corners ):
  """
    Use the centroid formula to compute the centroid
    of the polygon defined by these geopt_corners.

    Limitations:

    We make no attempt to account for the fake that this polygon
    may be self intersecting, while the formula is said to 
    only apply to non self intersecting polygons.
  """
  lat = 0.0
  long = 0.0
  
  

  return search.GeoPoint( lat, long )

def compute_radius( centroid, geopt_corners ):
  """
    Find the distance between the centroid and the furthest corner.
    Return that as the radius, all other corners are then 
    guaranteed to be within that circle centered on the centroid
    having that radius.
  """
  return 0.0

def create_geojson( props_dict, geopt_corners ):
  return json.dumps( {
      "type" : "Feature", 
      "geometry" : {
          "type": "Polygon",
          "coordinates": [ [ p.latitude, p.longitude ] for p in geopt_corners ]
        },
      "properties" : props_dict
    } )
