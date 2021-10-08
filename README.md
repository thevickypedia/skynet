# Skynet
Stock Alerter using Robinhood api

This script is designed to run locally using a env vars stored in a `.env` file which is loaded upon startup.

The stock ticker value, minimum amount below and maximum amount above which you'd like to be notified has to be added as env variables. 

Below is an example for a single stock, this can be extended up to monitoring 25 stocks.

- Example: 
    - stock_1 = AMZN
    - stock_1_min = 3000
    - stock_1_max = 4000

For notifications, store env vars as below (either in `.env` file or as regular env vars):
  - `gmail_user = xxx@yyy@gmail.com`
  - `gmail_pass = PASSWORD`
  - `phone = +1234567890`

## License & copyright

&copy; Vignesh Sivanandha Rao, Skynet

Licensed under the [MIT License](LICENSE)
