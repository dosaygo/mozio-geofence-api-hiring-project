import json

def to_dict( request, input_format ):
  if input_format == 'json':
    return json.loads( request.body )
  elif input_format == 'x-www-form-urlencoded':
    return request.params.mixed()
  elif input_format == 'x-search-api-doc':
    doc_dict = dict([ ( field.name, field.value ) for field in request.fields ])
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


