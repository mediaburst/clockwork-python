# Clockwork SMS API for Python

## Install

The easiest way to install is through "pip":
    
    pip install clockwork

## Requirements

* Python 2.6+
* [lxml][1] 

For an easy life, we recommend installing lxml thorugh a package manager, e.g.:
    
    sudo apt-get install python-lxml    # Debian based
    sudo yum install pyhton-lxml        # Red Hat based

## Usage

### Send a single SMS message

    from clockwork import clockwork
    api = clockwork.API('API_KEY_GOES_HERE')
    message = clockwork.SMS(to = '441234123456', message = 'This is a test message.')
    response = api.send(message)
    
    if response.success:
        print (response.id)
    else:
        print (response.error_code)
        print (response.error_description)
   
### Send multiple SMS messages

Simply pass an array of sms objects to the send method. Instead of sending back a single sms response, an array of sms responses will be returned:

    from clockwork import clockwork
    api = clockwork.API('API_KEY_GOES_HERE')
    message1 = clockwork.SMS(to = '441234123456', message = 'This is a test message 1.')
    message2 = clockwork.SMS(to = '441234123457', message = 'This is a test message 2.')
    message3 = clockwork.SMS(to = '441234123458', message = 'This is a test message 3.')
    response = api.send([message1,message2,message3])
    
    for sms_response in response:
        if sms_response.success:
            print (sms_response.id)
        else:
            print (sms_response.error_code)
            print (sms_response.error_description)
    
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

    api = clockwork.API('MY_API_KEY', from_name = 'Bobby')


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

    api = clockwork.API('MY_API_KEY',from_name = 'Bobby')
    sms = clockwork.SMS(to = '441234123456', message = 'This is a test message 1.', from_name = 'Sammy')
    response = api.send(sms) # WILL SEND WITH FROM ADDRESS 'Sammy'

### Check balance

    from clockwork import clockwork
    api = clockwork.API('API_KEY_GOES_HERE')
    balance = api.get_balance()
    print (balance) # => {'currency': None, 'balance': '231.03', 'account_type': 'PAYG'}


## License

This project is licensed under the MIT open-source license.

A copy of this license can be found in LICENSE.txt

## Contributing

If you have any feedback on this wrapper drop us an email to [hello@clockworksms.com][3].

The project is hosted on GitHub at [http://www.github.com/mediaburst/clockwork-python][4].

If you would like to contribute a bug fix or improvement please fork the project 
and submit a pull request. Please add tests for your use case.

[1]: http://lxml.de/
[2]: http://www.clockworksms.com/doc/clever-stuff/xml-interface/send-sms/
[3]: mailto:hello@clockworksms.com
[4]: http://www.github.com/mediaburst/clockwork-python

## Changelog

### 1.0.0 (01st August, 2013)

* Initial release of wrapper [MR]

### 1.0.1 (01st September, 2013)

* Minor changes

### 1.0.2 (18th May 2014)

* Unicode support added [MR]

## Credits and Acknowledgements

Many thanks to @cHemingway for adding Unicode support.
