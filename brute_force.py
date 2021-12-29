from data_processor import Data_Processor
from linear_regression import Linear_Regression


class Brute_Force:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.do_it()
        self.show_results()
        
    def do_it(self):
        self.results = {}
        for i in range(3, 181):
            Data_Processor(self.ticker, i)
            lr = Linear_Regression(self.ticker)
            self.results[i] = lr.test_score
            
    def show_results(self):
        self.sorted_results = dict(sorted(self.results.items(), key= lambda x:x[1]))
        print(self.sorted_results)

if __name__ == '__main__':
    Brute_Force("AMD")