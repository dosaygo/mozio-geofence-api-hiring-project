import json
import re

from google.appengine.api import search

def to_dict( request, input_format ):
  if input_format == 'json':
    return json.loads( request.body )
  elif input_format == 'x-www-form-urlencoded':
    return request.params.mixed()
  elif input_format == 'x-search-api-doc':
    doc_dict = dict([ to_basic_type( field.name, field.value ) for field in request.fields ])
    doc_dict[ 'id' ] = request.doc_id or ""
    return doc_dict
  else:
    raise TypeError( "Input format %s must be one of json or html. It is not." % input_format )
    
def from_dict( result, output_format ):
  if output_format == 'json':
    return json.dumps( result )
  elif output_format == 'html':
    return "<pre><code>%s</code></pre>" % json.dumps( result, 
                                                indent = 2,
                                                sort_keys = True )
  else:
    raise TypeError( "Output format %s must be one of json or html. It is not." % output_format )

def to_Search_API_GeoPoint( request, input_format ):
  if input_format == 'whitespace-gapped-pair':
    lat, long = request.split()
    lat, long = float( lat ), float( long )
    return search.GeoPoint( lat, long )
  if input_format == 'comma-gapped-pair':
    lat, long = re.split( r'\s*,\s*', request )
    lat, long = float( lat ), float( long )
    return search.GeoPoint( lat, long )
  else:
    raise TypeError( "Input format %s must be one of whitespace-gapped-pair or comma-gapped-pair. It is not." % input_format )

def to_list_of_Search_API_GeoPoints( request, input_format ):
  if input_format == 'comma-gapped-list/whitespace-gapped-pairs':
    return [ to_Search_API_GeoPoint( p, 'whitespace-gapped-pair' ) for p in re.split( r'\s*,\s*', request ) ]
  elif input_format == 'whitepsace-gapped-list/comma-gapped-pairs':
    return [ to_Search_API_GeoPoint( p, 'comma-gapped-pair' ) for p in request.split() ]
  else:
    raise TypeError( "Input format %s must be on of comma-gapped-list/whitespace-gapped-pairs or whitespace-gapped-list/comma-gapped-pairs. It is not." )

def to_Search_API_GeoPoint_or_raise( request ):
  errors = []
  try:
    geopoint = to_Search_API_GeoPoint( request, 'whitespace-gapped-pair' )
  except BaseException as e:
    errors.append( e )
  else:
    return geopoint
  try:
    geopoint = to_Search_API_GeoPoint( request, 'comma-gapped-pair' )
  except BaseException as e:
    errors.append( e )
    raise TypeError( "Errors when converting to GeoPoint: %s" % ( ';'.join(( str( x ) for x in errors ) ) ) )

def to_basic_type( name, value ):
  if isinstance( value, search.GeoPoint ):
    value = { "latitude" : value.latitude, "longitude" : value.longitude }
  return ( name, value )
