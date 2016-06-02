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


