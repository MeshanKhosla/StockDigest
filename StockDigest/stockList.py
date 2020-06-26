import os
from Stock import Stock

# Ticker, Bought Price, Shares bought
ownedStocks = {
    Stock("AAPL", 300, 2),      # Ex: Bought 2 shares of AAPL at $300 each
    Stock("GOOG", 1200.50, 1),  # Ex: Bought 1 share of GOOG at $1200.50

}

"""
E-mail and password
* Note: I have them set to environment variables, ut they can also be hard coded in
* email is the e-mail you want to receive the e-mail from
* send_to_email is the receiver of the e-mail
* I used the same e-mail to send and receive
"""
email = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
send_to_email = os.environ.get('EMAIL_ADDRESS')
