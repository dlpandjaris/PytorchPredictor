import pandas_datareader as pdr
from datetime import datetime
import requests

class Data_Getter:
    def __init__(self, ticker: str):
        self.ticker = ticker
        raw_data = self.get_raw_data()

    def get_raw_data(self):
        start = datetime(2008, 9, 30)
        end = datetime(2020, 1, 1)
        data = pdr.DataReader(self.ticker, 'yahoo', start, end)
        return(data)


def main():
    Data_Getter("AMD")


if __name__ == '__main__':
    #main()
    print(requests.get("https://www.yahoo.com"))