# coding: utf-8
try:
    import urllib.request as _urllib # py3
except ImportError:
    import urllib2 as _urllib # py2

from . import clockwork_exceptions

def request(url, xml):
    """Make a http request to clockwork, using the XML provided
       Sets sensible headers for the request.
    
       If there is a problem with the http connection a clockwork_exceptions.HttpException is raised
       """
    
    r = _urllib.Request(url, xml)
    r.add_header('Content-Type', 'application/xml')
    r.add_header('User-Agent', 'Clockwork Python wrapper/1.0')
    
    result = {}
    try:
        f = _urllib.urlopen(r)
    except _urllib.URLError as error:
        raise clockwork_exceptions.HttpException("Error connecting to clockwork server: %s" % error)
    
    result['data'] = f.read()
    result['status'] = f.getcode()
    
    if hasattr(f, 'headers'):
        result['etag'] = f.headers.get('ETag')
        result['lastmodified'] = f.headers.get('Last-Modified')
        if f.headers.get('content−encoding', '') == 'gzip':
            result['data'] = gzip.GzipFile(fileobj=StringIO(result['data'])).read()
        if hasattr(f, 'url'):
            result['url'] = f.url
            result['status'] = 200
    f.close()
    
    if result['status'] != 200:
        raise clockwork_exceptions.HttpException("Error connecting to clockwork server - status code %s" % result['status'])
    
    return result
