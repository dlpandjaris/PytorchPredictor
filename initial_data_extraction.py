import pandas_datareader as pdr
from datetime import datetime

class Data_Getter:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.raw_data = self.get_raw_data()
        self.reverse_data()
        self.save_to_file()

    def get_raw_data(self) -> pdr.DataReader:
        """Reads in raw data from yahoo finance"""
        start = datetime(2008, 9, 30)
        end = datetime.now() #(2020, 1, 1)
        data = pdr.DataReader(self.ticker, 'yahoo', start, end)
        return(data)
    
    def reverse_data(self):
        """Reverses row order in raw data"""
        self.raw_data = self.raw_data.iloc[::-1]
    
    def save_to_file(self):
        """Saves raw data to csv file"""
        self.raw_data.to_csv("{}_raw_data.csv".format(self.ticker))

def main():
    data = Data_Getter("AMD")
    print(data.raw_data)

if __name__ == '__main__':
    main()