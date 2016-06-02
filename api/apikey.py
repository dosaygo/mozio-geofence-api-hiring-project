import json

from google.appengine.api import search

from webapp2 import (
    WSGIApplication as Endpoint,
    Route as path
  )

from webapp2_extras.routes import (
    PathPrefixRoute as base
  )

import convert

from service import Service 

class APIKeyService( Service ):
  index = search.Index( 'apikey' )

  def makeDoc( self, params, doc_id = None ):
    return search.Document(
        doc_id = doc_id,
        fields = [
          search.TextField( name='name', value=params.get( 'name' ) ),
          search.AtomField( name='api_key', value=params.get( 'api_key' ) )
        ] )

endpoint = Endpoint( [
    base( r'/mozio-geofence', [
      path( r'/api/apikey', handler = APIKeyService ),
      path( r'/api/apikey/in/<input_format>', handler = APIKeyService ),
      path( r'/api/apikey/out/<output_format>', handler = APIKeyService ),
      path( r'/api/apikey/in/<input_format>/out/<output_format>', handler = APIKeyService )
    ] )
  ], debug = True )


