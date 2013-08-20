# Exception classes

class HttpException(Exception):
	def __init__(self, value):
	    self.value = value
	def __str__(self):
	    return repr(self.value)

class AuthException(Exception):
	def __init__(self, value):
	    self.value = value
	def __str__(self):
	    return repr(self.value)

class GenericException(Exception):
	def __init__(self, value):
	    self.value = value
	def __str__(self):
	    return repr(self.value)

class ApiException(Exception):
	def __init__(self, value, errNum):
	    self.value = value
	    self.errNum = errNum
	def __str__(self):
	    return repr(self.value)
