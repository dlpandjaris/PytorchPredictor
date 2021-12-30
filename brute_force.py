from data_processor import Data_Processor
from linear_regression import Linear_Regression


class Brute_Force:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.do_it()
        self.show_results()
        
    def do_it(self):
        self.results = {}
        for i in range(3, 6):
            Data_Processor(self.ticker, i)
            lr = Linear_Regression(self.ticker)
            self.results[i] = (lr.train_score, lr.test_score, lr.accuracy)
            print(i)
    
    def show_results(self):
        self.sorted_results = dict(sorted(self.results.items(), key= lambda x:x[-1]))
        print("Train R2, Test R2, Accuracy")
        for result in self.results.items():
            print(result)

if __name__ == '__main__':
    Brute_Force("AMD")