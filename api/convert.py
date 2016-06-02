import json

def to_dict( request, input_format ):
  if input_format == 'json':
    return json.loads( request.body )
  elif input_format == 'x-www-form-urlencoded':
    return request.params.mixed()
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
