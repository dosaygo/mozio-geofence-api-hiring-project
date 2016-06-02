from google.appengine.api import search

from webapp2 import (
    WSGIApplication as Endpoint,
    Route as path,
    RequestHandler as Service
  )

from webapp2_extras.routes import (
    PathPrefixRoute as base
  )

import convert

from service import Service


class TerritoryService( Service ):
  index = search.Index( 'territory' )

  def makeDoc( self, params, doc_id = None ):
    return search.Document(
        doc_id = doc_id,
        fields = [
          search.TextField( name='provider_name', value=params.get( 'provider_name' ) ),
          search.NumberField( name='service_price', value=float( params.get( 'service_price' ) ) ),
          search.TextField( name='corners', value=params.get( 'corners' ) )
        ] )

  def searchTerritoriesIntersectingLatLong( sef, lat, long ):
    """
      make a query string using lat long and 
      search for territories intersect
    """


endpoint = Endpoint( [
    base( r'/mozio-geofence', [
      path( r'/api/territory', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>', handler = TerritoryService ),
      path( r'/api/territory/out/<output_format>', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>/out/<output_format>', handler = TerritoryService )
    ] )
  ], debug = True )


