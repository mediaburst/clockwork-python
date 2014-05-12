# -*- coding: utf-8 -*-

import unittest
import clockwork
import clockwork_exceptions

class ApiTests(unittest.TestCase):

	api_key = "YOUR_API_KEY_HERE"

	def test_should_send_single_message(self):
		"""Sending a single SMS with the minimum detail and no errors should work"""
		api = clockwork.API(self.api_key)
		sms = clockwork.SMS(to="441234567890", message="This is a test message")
		response = api.send(sms)
		self.assertTrue(response.success)

	def test_should_send_single_unicode_message(self):
		"""Sending a single SMS with the full GSM character set (apart from ESC and form feed) should work"""
		api = clockwork.API(self.api_key)
		sms = clockwork.SMS(
            to="441234567890",
		    #Message table copied from http://www.clockworksms.com/doc/reference/faqs/gsm-character-set/
            #Note, the "/f" (form feed) character does not work as lxml prohibits it.
			message= 	u'''@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ'''
				 		u''' !“#¤%&‘()*+,-./'''
				        u'''0123456789:;<=>?'''
				        u'''¡ABCDEFGHIJKLMNO'''
				        u'''PQRSTUVWXYZÄÖÑÜ§'''
				        u'''¿abcdefghijklmno'''
				        u'''pqrstuvwxyzäöñüà'''
                        u'''€[\]^{|}~'''
			,long=True)
		response = api.send(sms)
		self.assertTrue(response.success)


	def test_should_fail_with_no_message(self):
		"""Sending a single SMS with no message should fail"""
		api = clockwork.API(self.api_key)
		sms = clockwork.SMS(to="441234567890", message="")
		response = api.send(sms)
		self.assertFalse(response.success)

	def test_should_fail_with_no_to(self):
		"""Sending a single SMS with no message should fail"""
		api = clockwork.API(self.api_key)
		sms = clockwork.SMS(to="", message="This is a test message")
		response = api.send(sms)
		self.assertFalse(response.success)

	def test_should_send_multiple_messages(self):
		"""Sending multiple sms messages should work"""
		api = clockwork.API(self.api_key)
		sms1 = clockwork.SMS(to="441234567890", message="This is a test message 1")
		sms2 = clockwork.SMS(to="441234567890", message="This is a test message 2")
		response = api.send([sms1,sms2])

		for r in response:
			self.assertTrue(r.success)

	def test_should_send_multiple_messages_with_erros(self):
		"""Sending multiple sms messages, one of which has an invalid message should work"""
		api = clockwork.API(self.api_key)
		sms1 = clockwork.SMS(to="441234567890", message="This is a test message 1")
		sms2 = clockwork.SMS(to="441234567890", message="")
		response = api.send([sms1,sms2])

		self.assertTrue(response[0].success)
		self.assertFalse(response[1].success)

	def test_should_fail_with_invalid_key(self):
		api = clockwork.API("this_key_is_wrong")
		sms = clockwork.SMS(to="441234567890", message="This is a test message 1")
		self.assertRaises(clockwork_exceptions.ApiException, api.send, sms)

	def test_should_be_able_to_get_balance(self):
		api = clockwork.API(self.api_key)
		balance = api.get_balance()
		self.assertEqual('PAYG',balance['account_type'])

if __name__ == "__main__":
	unittest.main()





