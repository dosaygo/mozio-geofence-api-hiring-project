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

class ProviderService( Service ):
  index = search.Index( 'provider' )

  def makeDoc( self, params, doc_id = None ):
    return search.Document(
        doc_id = doc_id,
        fields = [
          search.TextField( name='name', value=params.get( 'name' ) ),
          search.AtomField( name='email', value=params.get( 'email' ) ),
          search.AtomField( name='phone', value=params.get( 'phone' ) ),
          search.AtomField( name='lang', value=params.get( 'lang' ) ),
          search.AtomField( name='fiat', value=params.get( 'fiat' ) )
        ] )


endpoint = Endpoint( [
    base( r'/mozio-geofence', [
      path( r'/api/provider', handler = ProviderService ),
      path( r'/api/provider/in/<input_format>', handler = ProviderService ),
      path( r'/api/provider/out/<output_format>', handler = ProviderService ),
      path( r'/api/provider/in/<input_format>/out/<output_format>', handler = ProviderService )
    ] )
  ], debug = True )


