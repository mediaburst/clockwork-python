# coding: utf-8
import urllib2
import clockwork_exceptions

def request(url, xml):
	"""Make a http request to clockwork, using the XML provided
	   Sets sensible headers for the request.

	   If there is a problem with the http connection a clockwork_exceptions.HttpException is raised
	   """
	
	r = urllib2.Request(url, xml)
	r.add_header('Content-Type','application/xml')
	r.add_header('User-Agent','Clockwork Python wrapper/1.0')

	result = {}
	try:
		f = urllib2.urlopen(r)
	except urllib2.URLError as error:
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
