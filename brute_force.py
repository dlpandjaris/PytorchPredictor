from data_processor import Data_Processor
from linear_regression import Linear_Regression
from initial_data_extraction import Data_Getter
import pandas as pd


class Brute_Force:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.linear_regression()
        
    def linear_regression(self):
        self.results = {"Days Knowledge": [], "Train R2": [], "Test R2": [], "Profit": [], "Accuracy": []}
        Data_Getter(self.ticker)
        for i in range(3, 6):
            Data_Processor(self.ticker, i)
            lr = Linear_Regression(self.ticker)
            self.results["Days Knowledge"].append(i)
            self.results["Train R2"].append(lr.train_score)
            self.results["Test R2"].append(lr.test_score)
            self.results["Profit"].append(lr.profit)
            self.results["Accuracy"].append(lr.accuracy)
            self.save_results("Linear Regression")
            print(i)
    
    def save_results(self, sheet_name):
        df = pd.DataFrame(self.results)
        df = df.sort_values(by = ["Accuracy"], ascending=False)
        df.to_excel("Data/{}/{}_results.xlsx".format(self.ticker, self.ticker), sheet_name = sheet_name, index = False)

if __name__ == '__main__':
    Brute_Force("AMD")