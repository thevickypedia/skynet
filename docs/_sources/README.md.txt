# Skynet
Stock Alerter using Robinhood api

This script is designed to run locally using a env vars stored in a `.env` file which is loaded upon startup.

The stock ticker value, minimum amount below and maximum amount above which you'd like to be notified has to be added to a file: `stocks.json`. 

Below is an example for a single stock, this can be extended up to monitoring `7,500` stocks.

### Source File
```json
{
  "stock_1": "AMZN",
  "stock_1_min": 3000,
  "stock_1_max": 4000
}
```

### Env Variables
Store env vars as below (either in `.env` file or as regular env vars)

For stock analyzing:
  - `robinhood_user = xxx@yyy.com`
  - `robinhood_pass = <Robinhood Password>`
  - `robinhood_qr = <Robinhood QR Code>`

For notifications:
  - `gmail_user = xxx@yyy@gmail.com`
  - `gmail_pass = PASSWORD`
  - `phone = +1234567890`

### Coding Standards
Docstring format: [`Google`](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) <br>
Styling conventions: [`PEP 8`](https://www.python.org/dev/peps/pep-0008/) <br>
Clean code with pre-commit hooks: [`flake8`](https://flake8.pycqa.org/en/latest/) and 
[`isort`](https://pycqa.github.io/isort/)

### Linting
`PreCommit` will ensure linting, and the doc creation are run on every commit.

**Requirement**
<br>
`pip install --no-cache --upgrade sphinx pre-commit recommonmark`

**Usage**
<br>
`pre-commit run --all-files`

## License & copyright

&copy; Vignesh Sivanandha Rao, Skynet

Licensed under the [MIT License](LICENSE)
