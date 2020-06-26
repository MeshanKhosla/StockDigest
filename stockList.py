import os
from Stock import Stock

# Ticker, Bought Price, Shares bought
ownedStocks = {
    Stock("DRI", 75.24, 1),
    Stock("PLAY", 16.46, 4),
    Stock("AAPL", 289.82, 1),     
}

#  E-mail part
email = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
send_to_email = os.environ.get('EMAIL_ADDRESS')