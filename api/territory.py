import logging

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
import geofencesearch
from service import Service


class TerritoryService( Service ):
  index = search.Index( 'territory' )

  def makeDoc( self, params, doc_id = None ):
    geopt_corners = convert.to_list_of_Search_API_GeoPoints( params.get( 'corners' ), 'comma-gapped-list/whitespace-gapped-pairs' ) 
    centroid = geofencesearch.compute_centroid( geopt_corners )
    radius = geofencesearch.compute_radius( centroid, geopt_corners )
    return search.Document(
        doc_id = doc_id,
        fields = [
          search.TextField( name='provider_name', value=params.get( 'provider_name' ) ),
          search.NumberField( name='service_price', value=float( params.get( 'service_price' ) ) ),
          search.TextField( name='corners', value=params.get( 'corners' ) ),
          search.GeoField( name='centroid', value=centroid ),
          search.NumberField( name='radius', value=radius )
        ] )

  def searchTerritoriesIntersectingLatLong( sef, lat, long ):
    """
      make a query string using lat long and 
      search for territories intersect
    """

  def processRequest( self, action, params ):
    try:
      super( Service, self ).processRequest( action, params )
    except BaseException as e:
      logging.warn( "Action %s unsupported by superclass, Service. Attempting baseclass implementation." % action )

      if action == 'latlongsearch':
        geopoint = convert.to_Search_API_GeoPoint_or_raise( params.get( 'latlongquery' ) )
        query = "distance(centroid, geopoint(%s, %s)) < %s" % ( str( geopoint.latitude ), str( geopoint.longitude ), str( geofencesearch.MAX_TERRITORY_RADIUS_M ) )
        result = self.searchDoc( query ) 
        return [ convert.to_dict( doc, 'x-search-api-doc' ) for doc in result ]
      else:
        raise TypeError( "Action %s must be latlongsearch, or %s" % ( action, str( e ) ) )

endpoint = Endpoint( [
    base( r'/mozio-geofence', [
      path( r'/api/territory', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>', handler = TerritoryService ),
      path( r'/api/territory/out/<output_format>', handler = TerritoryService ),
      path( r'/api/territory/in/<input_format>/out/<output_format>', handler = TerritoryService )
    ] )
  ], debug = True )


