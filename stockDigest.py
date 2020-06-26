import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from yahoo_fin import stock_info as si
import pandas as pd
import datetime
from datetime import date
import time
from Stock import Stock
from stockList import ownedStocks, email, password, send_to_email

def getYesterdaysDate():
    yesterday = date.today() - datetime.timedelta(days=1)
    return yesterday.strftime("%m/%d/%y")

# Note: Needs to be tomorrow's date for yahoo_fin graph to include it today's price
def getTomorrowsDate():
    tomorrow = date.today() + datetime.timedelta(days=1)
    return tomorrow.strftime("%m/%d/%y")

# Global variables 
completeNet = 0
dailyNet = 0
netSinceBought = 0
diff = 0
messages = []

def updateNet():
    global completeNet
    global dailyNet
    global netSinceBought
    global diff
    global messages

    for stock in ownedStocks:
        # Gets price data of stock
        df = pd.DataFrame(si.get_data(stock.getTicker(), start_date = getYesterdaysDate() , end_date = getTomorrowsDate()))
        yesterdaysClosingPrice = df["adjclose"][0]
        todaysClosingPrice = df["adjclose"][1]
        boughtPrice = stock.getPurchPrice()

        # Adds todays price and price stock was bought for
        messages.append(f"{stock.getTicker()} closing price today: ${round(todaysClosingPrice, 3)}")
        messages.append(f"{stock.getTicker()} bought for: ${round(boughtPrice, 3)}")

        # Gets net from beginning
        netSinceBought = (todaysClosingPrice - boughtPrice)      # Finds net of each individual stock since it was originally bought
        completeNet += netSinceBought
        # Multiples by number of shares for total net
        messages.append(f"{stock.getTicker()} net since bought: ${round(netSinceBought * stock.getSharesBought(), 3)} (${round(netSinceBought, 3)} per share)")

        # Gets net since yesterday's closing price
        diff = (todaysClosingPrice - yesterdaysClosingPrice)
        dailyNet += diff
        messages.append(f"{stock.getTicker()} net since yesterday: ${round(diff * stock.getSharesBought(), 3)} (${round(diff, 3)} per share)\n")



def getMessage():
    updateNet()
    # Adds net since beginning, and net since yesterday
    messages.append(f"Portfolio net: ${round(completeNet, 3)}")
    messages.append(f"Daily net: ${round(dailyNet, 3)}")

    return '\n'.join(messages)



def send_mail():
    # Prepares e-mail
    msg = MIMEMultipart()
    message = getMessage()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = "Daily Stock Digest"
    msg.attach(MIMEText(message, 'plain'))

#   Sends e-mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print("Sent!")

if __name__ == '__main__':
    send_mail()
                                            