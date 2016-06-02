import json

from webapp2 import (
      WSGIApplication as Endpoint,
      Route as path,
      RequestHandler as Service
    )

class APIKeyService( Service ):

  def post( self, 
      input_format = 'x-www-form-urlencoded', 
      output_format = 'html' ):

    params = None
    result = None
    output = None

    # convert from input format
    if input_format == 'json':
      params = json.loads( self.request.body )
    elif input_format == 'x-www-form-urlencoded':
      params = self.request.params.mixed()
   
    # process input to output
    result = params

    # convert to output format
    if output_format == 'json':
      output = json.dumps( result )
    elif output_format == 'html':
      output = "<pre><code> %s </code></pre>" % json.dumps( result, 
                                                  indent = 2,
                                                  sort_keys = True )

    self.response.out.write( output )

endpoint = Endpoint( [
    path( r'/api/apikey', handler = APIKeyService ),
    path( r'/api/apikey/in/<input_format>', handler = APIKeyService ),
    path( r'/api/apikey/out/<output_format>', handler = APIKeyService ),
    path( r'/api/apikey/in/<input_format>/out/<output_format>', handler = APIKeyService )
  ], debug = True )


