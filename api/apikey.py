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

class APIKeyService( Service ):

  def createAPIKey( self, params ):
    """
      Create an APIKey doc and add it to the index
    """

  def deleteAPIKey( self, id ):
    """
      Delete an APIKey from the index by id
    """

  def searchAPIKey( self, query ):
    """ 
      Find an APIKey by querying the index 
    """

  def readAPIKey( self, id ):
    """
      Read an APIKey from the index by id
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
      path( r'/api/apikey', handler = APIKeyService ),
      path( r'/api/apikey/in/<input_format>', handler = APIKeyService ),
      path( r'/api/apikey/out/<output_format>', handler = APIKeyService ),
      path( r'/api/apikey/in/<input_format>/out/<output_format>', handler = APIKeyService )
    ] )
  ], debug = True )


