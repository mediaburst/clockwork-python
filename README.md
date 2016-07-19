# Clockwork SMS API for Python

## Install

The easiest way to install is through "pip":

    pip install clockwork

## Requirements

* Python 2.6+

## Usage

### Send a single SMS message

```python
from clockwork import clockwork
api = clockwork.API('API_KEY_GOES_HERE') #Be careful not to post your API Keys to public repositories.
message = clockwork.SMS(to = '441234123456', message = 'This is a test message.')
response = api.send(message)

if response.success:
    print (response.id)
else:
    print (response.error_code)
    print (response.error_message)
```

### Send multiple SMS messages

Simply pass an array of sms objects to the send method. Instead of sending back a single sms response, an array of sms responses will be returned:

```python
from clockwork import clockwork
api = clockwork.API('API_KEY_GOES_HERE') #Be careful not to post your API Keys to public repositories.
message1 = clockwork.SMS(to = '441234123456', message = 'This is a test message 1.')
message2 = clockwork.SMS(to = '441234123457', message = 'This is a test message 2.')
message3 = clockwork.SMS(to = '441234123458', message = 'This is a test message 3.')
response = api.send([message1,message2,message3])

for sms_response in response:
    if sms_response.success:
        print (sms_response.id)
    else:
        print (sms_response.error_code)
        print (sms_response.error_message)
```

Passing an array of messages to the send method is much more efficient than making multiple calls to the `send` method; as well making less round-trips to the server the messages are "batched" in clockwork, which is significantly better for performance.

### Send messages - available parameters

This wrapper supports a subset of the available clockwork API parameters for sending  (for the full set see [here][2]).

##### Setting parameters for all messages

You create an `api` object with `api = clockwork.API(api_key,[optional_setting = value,..]`
The `optional_setting` parameters allows you to set the following, which will be used for all messages sent through the `api` object:

Parameter | Description
--------- | -----------
from_name | Sets the [from name](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-from "from address")
concat | Sets the [concat](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-concat) setting
invalid_char_option | Sets the [InvalidCharOption](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-invalidcharaction) setting
truncate | Sets the [truncate](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-truncate) setting

So for example if I want all messages to use the from address 'bobby', I would do:

```python
    api = clockwork.API('MY_API_KEY', from_name = 'Bobby') 
```

##### Setting parameters for each message.

You create an `sms` object with `sms = clockwork.SMS(to = 'xxx', message = 'xxx', [optional_setting = value,..]`

In a similar pattern to the API parameters, the `optional_setting` parameters allows you to set the following additional parameters for an individual message:

Parameter | Description
--------- | -----------
client_id | Sets the [ClientId](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-clientid) setting
from_name | Sets the [from name](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-from "from address")
invalid_char_option | Sets the [InvalidCharOption](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-invalidcharaction) setting
truncate | Sets the [truncate](http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/#param-truncate) setting

Any parameters defined here will take precedence over the same one defined on the `api` object:

```python
api = clockwork.API('MY_API_KEY',from_name = 'Bobby')
sms = clockwork.SMS(to = '441234123456', message = 'This is a test message 1.', from_name = 'Sammy')
response = api.send(sms) # WILL SEND WITH FROM ADDRESS 'Sammy'
```

### Check balance

```python
from clockwork import clockwork
api = clockwork.API('API_KEY_GOES_HERE')  #Be careful not to post your API Keys to public repositories.
balance = api.get_balance()
print (balance) # => {'currency': None, 'balance': '231.03', 'account_type': 'PAYG'}
```

## License

This project is licensed under the MIT open-source license.

A copy of this license can be found in LICENSE.txt

## Contributing

If you have any feedback on this wrapper drop us an email to [hello@clockworksms.com][3].

The project is hosted on GitHub at [http://www.github.com/mediaburst/clockwork-python][4].

If you would like to contribute a bug fix or improvement please fork the project
and submit a pull request. Please add tests for your use case.

[2]: http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/
[3]: mailto:hello@clockworksms.com
[4]: http://www.github.com/mediaburst/clockwork-python

## Changelog

### 1.2.0 (24th February 2016)

* Removed lxml dependency
 
### 1.1.0 (5th January 2015)

* Python3 Support

### 1.03 (23rd December 2014)

* Replacing Distribute with Setuptools

### 1.0.2 (18th May 2014)

* Unicode support added [MR]

### 1.0.1 (01st September, 2013)

* Minor changes

### 1.0.0 (01st August, 2013)

* Initial release of wrapper [MR]


## Credits and Acknowledgements

Thanks to [zeroSteiner](https://github.com/zeroSteiner) for removing the lxml dependency and bringing ElementTree into the wrapper.

Thanks to [bjornpost](https://github.com/bjornpost) for his work on Python 3 support and replacing Distribute with Setuptools

Many thanks to [cHemingway](https://github.com/cHemingway) for adding Unicode support.
