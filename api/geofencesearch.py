from google.appengine.api import search

import convert

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

