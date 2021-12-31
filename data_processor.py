import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class Data_Processor:
    def __init__(self, ticker: str, days_knowledge: int):
        self.ticker = ticker
        self.days_knowledge = days_knowledge
        self.filename: str = ticker + "_raw_data.csv"
        self.raw_data: pd.DataFrame = self.read_raw_data()
        self.X_data: pd.DataFrame = self.generate_X_data()
        self.Y_data: pd.DataFrame() = self.generate_Y_data()
        self.final_df : pd.DataFrame() = self.join_data()
        self.add_profit_columns()
        self.write_test_train_csv()
    
    def read_raw_data(self) -> pd.DataFrame:
        """Records raw data from csv file"""
        data = pd.read_csv("Data/{}/{}".format(self.ticker, self.filename))
        return(data)
        
    def chop_X_data(self) -> List[pd.DataFrame]:
        """Chops raw_data into overlapping chunks of rows of size days_knowledge"""
        df_list = []
        columns = ["High", "Low", "Open", "Close", "Volume"]
        for index, row in self.raw_data.iterrows():
            if index > len(self.raw_data) - self.days_knowledge:
                break
            if index == 0:
                continue
            data = pd.DataFrame(columns=columns)
            for column in columns:
                data[column] = self.raw_data[column].iloc[index:index+self.days_knowledge]
            df_list.append(data)
            # if index == 2:
            #     break
        return(df_list)
    
    def generate_X_columns(self, df_list) -> List[str]:
        """Returns column list with duplicates for each day of knowledge"""
        starter_columns = df_list[0].columns
        return ["{}-{}".format(column, i) for column in starter_columns for i in range(1, self.days_knowledge+1)]
    
    def generate_X_data(self) -> pd.DataFrame:
        """Takes df list from chop_X_data and flattens each into one row"""
        df_list = self.chop_X_data()
        columns = self.generate_X_columns(df_list)
        new_df_list = []
        for df in df_list:
            new_row = []
            for column in df.columns:
                for val in df[column]:
                    new_row.append(val)
            new_df_list.append(new_row)
        new_df = pd.DataFrame(new_df_list, columns=columns)
        return(new_df)
    
    def generate_Y_data(self) -> pd.DataFrame:
        """Slices Close Column of raw data and cuts off edge days"""
        return self.raw_data.Close.iloc[:-self.days_knowledge]
        
    def join_data(self) -> pd.DataFrame():
        """Joins X data and Y data"""
        data = self.X_data.copy()
        data["Close-0"] = self.Y_data
        return data

    def add_profit_columns(self):
        """Makes percentage change column"""
        self.final_df["Profit"] = (self.final_df["Close-0"] / self.final_df["Close-1"]) - 1
        self.final_df["Profit-Bool"] = np.where(self.final_df["Profit"] > 0, "profit", "loss")
    
    def write_test_train_csv(self):
        """Generates csv file given a data frame"""
        self.final_df.to_csv("Data/{}/{}_test_train_data.csv".format(self.ticker, self.ticker), index=False)


def main():
    data = Data_Processor("AMD", 10)
    print(data.raw_data.iloc[-1])
    print(data.X_data)

if __name__ == '__main__':
    main()