
import json
import math

from google.appengine.api import search

"""
  Limitations:

    1. Providers can only enter a single territory whose set of points does not result in a radius larger than 250 m. So providers need to enter their territories in a piecemeal fashion. 

    2. When searching for a latitude and longitude we return all territories whose centre of operations ( as defined by the centroid in the polygon of the territory corners ), is within the maximum radius of a territory. So this means that the territories so returned, are not guaranteed to intersect with the given point, tho they are guaranteed to be within ( or more strictly, to have their centres within ) MAX_TERRITORY_RADIUS of the given point. 
"""

MAX_TERRITORY_RADIUS_M = 250

def convertWGS84ToGoogleBing( geopt ):
  """
    This is taken from here: https://alastaira.wordpress.com/2011/01/23/the-google-maps-bing-maps-spherical-mercator-projection/

    We use it to convert between co-ordinate systems, so we can use the x, y system ( planar projection ), to compute centroids.
  """
  lat, lon = geopt.latitude, geopt.longitude
  x = lon * 20037508.34 / 180 
  y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
  y = y * 20037508.34 / 180
  return [ x, y ]

def convertGoogleBingToWGS84( xy ):
  """
    This is taken from here: https://alastaira.wordpress.com/2011/01/23/the-google-maps-bing-maps-spherical-mercator-projection/

    We use it to convert between co-ordinate systems, so we can use the x, y system ( planar projection ), to compute centroids.

    We convert back to lat long to get our GeoPoints.
  """
  x, y = xy[ 0 ], xy[ 1 ]
  lon = (x / 20037508.34) * 180
  lat = (y / 20037508.34) * 180
  lat = 180/math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
  return search.GeoPoint( lat, lon ) 

def convert_geopoints_to_planar( geopt_corners ):
  return [ convertWGS84ToGoogleBing( p ) for p in geopt_corners ]

def convert_planars_to_geopoints( planars ):
  return [ convertGoogleBingToWGS84( p ) for p in planars ] 

def compute_graham_scan( geopt_corners ):
  """
    Attempt to clean the data,
    and simplify it to an approximate shape
    by returning the list of corners 
    corresponding to the convex hull of the
    given points.

    It attempts this using the Graham Scan
  """
  pass

def compute_area( geopt_corners ):
  """
    Compute the signed polygon area
  """
  pass

def compute_centroid( geopt_corners ):
  """
    Use the centroid formula to compute the centroid
    of the polygon defined by these geopt_corners.

    Limitations:

    We make no attempt to account for the fake that this polygon
    may be self intersecting, while the formula is said to 
    only apply to non self intersecting polygons.

    Additional notes:

    We make no assumptions as to the cleanness of the points given. So we attempt to clean the data by finding the convex hull of the points using a Graham Scan O ( n log n ), this eliminates points inside the hull.

    We then use the centroid formula for a polygon which also requires computing the signed area, to compute the centroid. 

    This causes a number of approximations. Concave features of the territory are lost, and as much as possible the set of points becomes closer in area to a circle. This is because the convex hull of a set of points the same shape obtained as if you were to stretch a rubber band around all the points and then let it tighten over them. The good point about this approximation is that there is never any point inside the territory which will be outside of our circle. However, there are points inside the circle which are not in the territory. The consequence is we will never fail to retrieve a territory given a point. Tho we will also retrieve territories that do not directly intersect the point but which are neighbours to it. This in itself is useful. And we can rank the territories returned by the distance of their centroid to the point. 

    This guarantees scalability and fast query speed and straightforward implementation. The cost of this method is accuracy as described above. It seems a reasonable cost, especially considering that retrieving neighbouring territories is also likely useful. A second important cost is that all territories input by providers must be less than the maximum radius. This radius determines the looseness of the groups. The smaller the radius, the tighter the groups, the larger the radius, the looser the groups returned in a query of a given point. The smaller it is, the tighter the groups of results obtained. Yet it is also a trade off, as the larger it is, the larger the territories that can be input. A workable choice can be decided by balancing these two considerations given knowledge of the real world uses, requirements and nature of the territory database.  
  """
  lat = 0.0
  long = 0.0
  
  

  return ( lat, long )

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

