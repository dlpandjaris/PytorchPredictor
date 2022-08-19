import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Linear_Regression:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.df = pd.read_csv("../Data/{}/{}_test_train_data.csv".format(ticker, ticker))
        self.preprocess()
        self.train()
        self.rate()
        
    def preprocess(self):
        self.X = self.df.iloc[:,:-3]
        self.y = self.df["Profit"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.25)
        
    def train(self):
        self.lr = LinearRegression()
        self.lr.fit(self.X_train, self.y_train)
                
    def rate(self):
        self.train_score = self.lr.score(self.X_train, self.y_train)
        self.test_score = self.lr.score(self.X_test, self.y_test)
        self.y_pred = self.lr.predict(self.X_test)
        
        correct = 0
        for actual, expected in list(zip(self.y_test, self.y_pred)):
            if actual > 0 and expected > 0:
                correct += 1
            elif actual < 0 and expected < 0:
                correct += 1
        self.accuracy = correct / len(self.y_test)
        
        self.profit = 0
        for actual, expected in list(zip(self.y_test, self.y_pred)):
            if expected > 0:
                self.profit += actual

if __name__ == "__main__":
    Linear_Regression("AMD")