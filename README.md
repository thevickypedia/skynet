# Skynet
Stock Alerter using Robinhood api

This script is designed to be run only on AWS using all the parameters received from SSM in the [aws_client](lib/aws_client.py) file.

The stock ticker value, minimum amount below and maximum amount above which you'd like to be notified has to be added as env variables in the lambda function. 

Below is an example which can be extended up to monitoring 25 stocks.

- Example: 
    - stock_1 = AMZN
    - stock_1_min = 3000
    - stock_1_max = 4000
    
Refer [stock_hawk](https://github.com/thevickypedia/stock_hawk/wiki#1-below-are-the-parameters-that-has-to-be-on-your-aws-ssm) for other setup instructions.

## License & copyright

&copy; Vignesh Sivanandha Rao, Skynet

Licensed under the [MIT License](LICENSE)
