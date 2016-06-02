import json

from google.appengine.api import search

from webapp2 import (
    RequestHandler as BaseService
  )

import convert

class Service( BaseService ):
  def createDoc( self, params ):
    """  
      Create the document and add it to the Provider index.
    """
    doc = self.makeDoc( params )
    result = self.index.put( doc )
    # we are only putting 1 doc, so get its id so we can return it
    return self.makeDoc( params, result[ 0 ].id )

  def deleteDoc( self, id ):
    """
      Delete the document by its id.
    """
    self.index.delete( id )

  def updateDoc( self, doc ):
    """
      Save the modified provider doc to the index.
    """
    self.index.put( doc )

  def readDoc( self, id ):
    """
      Read the provider document by id.
    """
    return self.index.get( id )
  
  def searchDoc( self, query ):
    """
      Search the provider index using a query.
    """
    results = self.index.search( query )
    return list( results )

  def processRequest( self, action, params ):
    if action == 'create':
      result = self.createDoc( params )
      return convert.to_dict( result, 'x-search-api-doc' )
    elif action == 'delete':
      return self.deleteDoc( params.get( 'id' ) )
    elif action == 'update':
      return self.updateDoc( self.makeDoc( params, params.get( 'id' ) ) )
    elif action == 'search':
      result = self.searchDoc( params.get( 'query' ) )
      return [ convert.to_dict( doc, 'x-search-api-doc' ) for doc in result ]
    elif action == 'read':
      return self.readDoc( params.get( 'id' ) )
    else:
      raise TypeError( "Action %s must be one of create, delete, update, search or read. It is not." )

  def post( self, 
      input_format = 'x-www-form-urlencoded', 
      output_format = 'html' ):

    params = None
    result = dict()
    output = None

    # convert from input format
    params = convert.to_dict( self.request, input_format )
    action = params.get( 'action' )
    # process input to output
    result = self.processRequest( action, params )
    # convert to output format
    output = convert.from_dict( result, output_format )
    self.response.out.write( output )
