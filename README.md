![logo](https://www.shipbob.com/wp-content/uploads/2021/04/shippo_logo_200x200-1.png)
# Shippo TSE Challange For Joshua Sternfeld

> The shippo TSE challange for Joshua Sternfeld - Technology Support Engineer

> I had a lot of fun learning your platform! 

## Information about challange (SQL)

Please notice that there is a Shippo - Josh Sternfeld (SQL).txt file. The .txt file is for the SQL answers. 

## Installing / Getting started

```shell
git clone https://github.com/hammy414/shippo
main.py start
```

The main.py file will show you your shipment info. If you want to change package information, please edit the file to do so. 

## Initial Configuration

In order to run shippo, you need to have the library installed. I recommend using pip to easily install that into your directory. Please see below link for the shippo library install. 

You will also need a shippo token, this can be obtained by your dashboard. I used a testing token to do this for free. 

This project I created pulls from a private isolated token. What you need to do is to create a new python file in the same directory called "shippo_secrets". After that create a method on that new file called "test_api_key= "REPLACE_WITH_YOUR_KEY"".

I have included a blank shippo_secrets file for you to use a template. 

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Links

- Shippo API Call Overview: https://goshippo.com/docs/reference/py#overview
- Shippo Into page for overview: https://goshippo.com/docs/intro/
- Shippo Library Install: https://goshippo.com/docs/client-libraries/
- Shippo Data Flow SQL: https://shippo-static.s3.amazonaws.com/img/illustrations/api-object-flow.png

## Licensing

The code in this project is licensed under creative commons license.
