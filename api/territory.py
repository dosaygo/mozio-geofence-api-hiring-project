from webapp2 import (
      WSGIApplication as Endpoint,
      Route as path,
      RequestHandler as Service
    )

class TerritoryService( Service ):
  def post( self ):
    self.response.out.write( "OORAH" )

endpoint = Endpoint( [
    path( r'/api/territory', handler = TerritoryService )
  ], debug = True )


