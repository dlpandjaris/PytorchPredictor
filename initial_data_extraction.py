import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))

# import pandas_datareader as pdr
# from datetime import datetime

# class Data_Getter:
#     def __init__(self, ticker):
#         ticker: str
#         raw_data = self.get_raw_data()

#     def get_raw_data(self):
#         start = datetime(2008, 9, 30)
#         end = datetime.now()
#         data = pdr.DataReader(self.ticker, 'yahoo', start, end)
#         return(data)


# def main():
#     Data_Getter("AMD")


# if __name__ == '__main__':
#     main()