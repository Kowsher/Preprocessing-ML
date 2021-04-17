
import pandas as pd


class MultiColumnOneHotEncoder:
    def __init__(self):
        pass # array of column names to encode

    def fit(self, df):
        self.df= df
        self.dummies_frame = pd.get_dummies(self.df)
        
        return self # not relevant here

    def transform(self, df2):
        if isinstance(df2, pd.DataFrame):
            df2 = pd.get_dummies(df2)
            df2 = df2.reindex(columns = self.dummies_frame.columns, fill_value=0)
            return df2
        else:
            team = pd.DataFrame(df2) 
            team.columns =list(self.df.columns)
            df2 = pd.get_dummies(team)
            df2 = df2.reindex(columns = self.dummies_frame.columns, fill_value=0)
            return df2

        

    def fit_transform(self,df):
        self.fit(df)
        return self.dummies_frame

