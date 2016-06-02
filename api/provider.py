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

class ProviderService( Service ):

  def createProvider( self, params ):
    """  
      Create the document
    """
    asdas
    """ create the document """
    sdsdfsfd
    """ add it to index """
    asdasds

  def deleteProvider( self, id ):
    """
      Delete the document
    """
    """ remove the document from index """

  def updateProvider( self, doc ):
    """
      Save the modified provider doc to the index
    """
    """ save to index """

  def readProvider( self, id ):
    """
      read the provider document by id
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
      path( r'/api/provider', handler = ProviderService ),
      path( r'/api/provider/in/<input_format>', handler = ProviderService ),
      path( r'/api/provider/out/<output_format>', handler = ProviderService ),
      path( r'/api/provider/in/<input_format>/out/<output_format>', handler = ProviderService )
    ] )
  ], debug = True )


