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

For more information on the available optional parameters for the SMS and API classes, see [here][2]. 

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