# Skynet
Stock Alerter using `Robinhood`/`YFinance` api

The stock ticker value, minimum amount below and maximum amount above which you'd like to be notified has to be added to a file: `stocks.json`. 

Below is an example for a single stock, this can be extended as needed.

### Source File
> Minimum and maximum values for the stock can be either a list or a comma separated string.
> The order doesn't matter.
```json
{
  "AMZN": [4000, 3000],
  "TSLA": "1000, 1400"
}
```
### Env Variables

This script is designed to run locally using env vars stored in a `.env` file which is loaded upon startup.

Store env vars as below (either in `.env` file or as regular env vars)

For stock analyzing:
  - `robinhood_user = xxx@yyy.com`
  - `robinhood_pass = <Robinhood Password>`
  - `robinhood_qr = <Robinhood QR Code>`

> :bulb: &nbsp; Skynet can work even without `Robinhood` access, as it automatically chooses `YahooFinance` to gather the details.
> However using `YahooFinance` runs longer due to endpoint restrictions.

For notifications:
  - `gmail_user = xxx@gmail.com`
  - `gmail_pass = PASSWORD`
  - `phone = +1234567890`

> :bulb: &nbsp; Phone numbers can be `comma` separated values, to notify multiple people.
> If notifications via [`gmail-connector`](https://github.com/thevickypedia/gmail-connector) fails, an SMS is triggered using AWS SNS.

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

### Runbook
[![made-with-sphinx-doc](https://img.shields.io/badge/Code%20Docs-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html)

[https://thevickypedia.github.io/gmail-connector/](https://thevickypedia.github.io/gmail-connector/)

## License & copyright

&copy; Vignesh Sivanandha Rao, Skynet

Licensed under the [MIT License](https://github.com/thevickypedia/skynet/blob/master/LICENSE)
