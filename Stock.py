class Stock:
    def __init__(self, ticker, purchPrice, sharesBought):
        self.ticker = ticker
        self.purchPrice = purchPrice
        self.sharesBought = sharesBought

    def getTicker(self):
        return self.ticker

    def getPurchPrice(self):
        return self.purchPrice

    def getSharesBought(self):
        return self.sharesBought