# StockDigest

This Python Script sends an e-mail to yourself updating you on how all of your stocks have done since you bought them, and how they did in the the trading day.

Example:

![Example](https://i.gyazo.com/bf63a15a16bd7692dffc5b9c9ec7361f.png)

## You only need to modify stockList.py

### Steps:
#### [Instructions/Demo](https://www.youtube.com/watch?v=prX_Wbd0nuI)
**1. Pull/download repo to your editor**
**2. Edit stockList.py with the current stocks you own or want to keep track of**

![owned stocks](https://i.gyazo.com/e3817b0300091fe1e6fb73bafaaa85b9.png)

Add a stock in the 'ownedStocks' dictionary

    Stock("AAPL", 300, 2)
    
This means that you bought 2 shares of AAPL at $300.00 each

**3. Add e-mail and password**

![e-mail/password](https://i.gyazo.com/c4e1db857b7e3059edee6ac8e0b197f2.png)

Although you can hard code the values in, I would suggest storing them in environment variables. [Windows](https://www.youtube.com/watch?v=IolxqkL7cD8) - [Mac/Linux](https://www.youtube.com/watch?v=5iWhQWVXosU)


Now you can run stockDigest.py and receive an e-mail update on how your stocks have performed!
If you want to set this program to run on a schedule, ie: every day when the stock market closes, set a task scheduler or cron task.

<details>
  <summary>Windows</summary>
  
  [Task Scheduler](https://www.youtube.com/watch?v=n2Cr_YRQk7o)
  
  _Note: Try these settings on the Actions page. The ones in the video did not work for me. The 'Start in' is the location of the file_
  
  ![Actions](https://i.gyazo.com/72aac915c077f32d4d81c0deace13689.png)
  
  Triggers:
  
  ![Triggers](https://i.gyazo.com/e8b2b0cf00b382c39aa4abad9d7b578b.png)
  
  The Stock market closes at 1:00 PST which is why I have 1:00. I also put the day after the current day as the first run time.
  
  You can also select 'Wake the computer to run this task' in the conditions page to wake the computer. This may require you to Enable Wake Timers in your control panel.
</details>

<details>
  <summary>Mac</summary>
  
  [Cron tasks](https://www.youtube.com/watch?v=Q2CNZGEH59Q)
  
  I do not own a Mac, so unfortunately you will need to look up any issues you may encounter :(
</details>

