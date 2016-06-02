import json

from webapp2 import (
    WSGIApplication as Endpoint,
    Route as path,
    RequestHandler as Service
  )

from webapp2_extras.routes import (
    PathPrefixRoute as base
  )

import convert

class TerritoryService( Service ):

  def searchTerritory( self, query ):
    """ 
      search for a territory by query string
    """

  def searchTerritoriesIntersectingLatLong( sef, lat, long ):
    """
      make a query string using lat long and 
      search for territories intersect
    """

  def createTerritory( self, params ):
    """
      Create a territory document and add it to the index
    """

  def updateTerritory( self, doc ):
    """
      Save the updated territory doc to an index
    """

  def deleteTerritory( self, id ):
    """
      Delete the territory from the index by id
    """

  def readTerritory( self, id ):
    """
      Get the territory from the index by id
    """

  def post( self, 
      input_format = 'x-www-form-urlencoded', 
      output_format = 'html' ):

    params = None
    result = None
    output = None

    # convert from input format
    params = convert.to_dict( self.request, input_format )

    # process input to output
    result = params

    # convert to output format
    output = convert.from_dict( params, output_format )

    self.response.out.write( output )

endpoint = Endpoint( [
    base( r'/mozio-geofence', [
      path( r'/api/territory', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>', handler = TerritoryService ),
      path( r'/api/territory/out/<output_format>', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>/out/<output_format>', handler = TerritoryService )
    ] )
  ], debug = True )


