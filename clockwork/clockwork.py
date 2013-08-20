from lxml import etree
import clockwork_http 
import clockwork_exceptions

SMS_URL = 'https://api.clockworksms.com/xml/send.aspx'
CREDIT_URL = 'https://api.clockworksms.com/xml/credit.aspx'
BALANCE_URL = 'https://api.clockworksms.com/xml/balance.aspx'


class SMS(object):
	"""An SMS object"""

	def __init__(self, to, message, client_id = None, from_name = None, long = None, truncate = None, invalid_char_option = None):
		self.client_id = client_id
		self.from_name = from_name
		self.long = long
		self.truncate = truncate
		self.invalid_char_option = invalid_char_option
		self.to = to
		self.message = message

class SMSResponse(object):
	"""An wrapper around an SMS reponse"""

	def __init__(self, sms, id, error_code, error_message, success):
		self.sms = sms
		self.id = id
		self.error_code = error_code
		self.error_message = error_message
		self.success = success


class API(object):
	"""Wraps the clockwork API"""
	def __init__(self, apikey, from_name = 'Clockwork', concat = 3, 
		invalid_char_option = 'error', long = False, truncate = True, 
		use_ssl = True):
		self.apikey = apikey
		self.from_name = from_name
		self.concat = concat
		self.invalid_char_option = invalid_char_option
		self.long = long
		self.truncate = truncate
		self.use_ssl = use_ssl

	def get_balance(self):
		"""Check the balance fot this account.
		   Returns a dictionary containing:
		   account_type: The account type
		   balance: The balance remaining on the account
		   currency: The currency used for the account balance. Assume GBP in not set"""
		
		xml_root = self.__init_xml('Balance')

		response = clockwork_http.request(BALANCE_URL,etree.tostring(xml_root))
		data_etree = etree.fromstring(response['data'])

		err_desc = data_etree.find('ErrDesc')	
		if err_desc is not None:
			raise clockwork_exceptions.ApiException(err_desc.text, data_etree.find('ErrNo').text)


		result = {}
		result['account_type'] = data_etree.find('AccountType').text
		result['balance'] = data_etree.find('Balance').text
		result['currency'] = data_etree.find('Currency').text
		return result

	def send(self, messages):
		"""Send a SMS message, or an array of SMS messages"""

		tmpSms = SMS(to='', message='')
		if str(type(messages)) == str(type(tmpSms)):
			messages = [messages]

		xml_root = self.__init_xml('Message')
		wrapper_id = 0

		for m in messages:
			m.wrapper_id = wrapper_id
			msg = self.__build_sms_data(m)
			sms = etree.SubElement(xml_root, 'SMS')
			for sms_element in msg:
				element = etree.SubElement(sms,sms_element)
				element.text = msg[sms_element]

		# print etree.tostring(xml_root)
		response = clockwork_http.request(SMS_URL,etree.tostring(xml_root))
		response_data = response['data']

		# print response_data
		data_etree = etree.fromstring(response_data)

		# Check for general error
		err_desc = data_etree.find('ErrDesc')	
		if err_desc is not None:
			raise clockwork_exceptions.ApiException(err_desc.text, data_etree.find('ErrNo').text)

		# Return a consistent object
		results = []
		for sms in data_etree:
			matching_sms = next((s for s in messages if str(s.wrapper_id) == sms.find('WrapperID').text),None)
			new_result = SMSResponse(
				sms = matching_sms,
				id = '' if sms.find('MessageID') is None else sms.find('MessageID').text,
				error_code = 0 if sms.find('ErrNo') is None else sms.find('ErrNo').text,
				error_message = '' if sms.find('ErrDesc') is None else sms.find('ErrDesc').text,
				success = True if sms.find('ErrNo') is None else (sms.find('ErrNo').text == 0) 
			)
			results.append(new_result)

		if len(results) > 1:
			return results
		else:
			return results[0]

	def __init_xml(self,rootElementTag):
		"""Init a etree element and pop a key in there"""
		xml_root = etree.Element(rootElementTag)
		key = etree.SubElement(xml_root, "Key")
		key.text = self.apikey
		return xml_root


	def __build_sms_data(self, message):
		"""Build a dictionary of SMS message elements"""

		attributes = {}
		
		attributes_to_translate = {
		'to' : 'To',
		'message' : 'Content',
		'client_id' : 'ClientID',
		'concat' : 'Concat',
		'from_name': 'From',
		'invalid_char_option' : 'InvalidCharOption',
		'truncate' : 'Truncate',
		'wrapper_id' : 'WrapperId'
		}

		for attr in attributes_to_translate:
			val_to_use = None
			if hasattr(message, attr):
				val_to_use = getattr(message,attr)
			if val_to_use == None and hasattr(self,attr):
				val_to_use = getattr(self,attr)
			if val_to_use != None:
				attributes[attributes_to_translate[attr]] = str(val_to_use)

		return attributes
		