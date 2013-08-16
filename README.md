# Clockwork SMS API for Python

## Install

Clone the library from github. Currently there is no package that you can get from a package manager such as pip.

## Requirements

Python 2.6+
[lxml][4] 

## Usage

For more information on the available optional parameters for the API (Clockwork::API), see [here][4].

For more information on the available optional parameters for each SMS (Clockwork::SMS), see [here][5]. For more information on the response object returned from each SMS (Clockwork::SMS::Response), see [here][6].

### Send a single SMS message

    import 'clockwork'
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

    import 'clockwork'
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

    import 'clockwork'
    api = clockwork.API('API_KEY_GOES_HERE')
    balance = api.get_balance()
    print (balance) # => {'currency': None, 'balance': '231.03', 'account_type': 'PAYG'}

## License

This project is licensed under the ISC open-source license.

A copy of this license can be found in LICENSE.

## Contributing

If you have any feedback on this wrapper drop us an email to [hello@clockworksms.com][2].

The project is hosted on GitHub at [http://www.github.com/mediaburst/clockwork-python][3].

If you would like to contribute a bug fix or improvement please fork the project 
and submit a pull request. Please add tests for your use case.

[1]: http://rubydoc.info/github/mediaburst/clockwork-python/master/frames
[2]: mailto:hello@clockworksms.com
[3]: http://www.github.com/mediaburst/clockwork-python
[4]: http://lxml.de/

## Changelog

### 1.0.0 (01st August, 2013)

* Initial release of wrapper [MR]