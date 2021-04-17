from sklearn.preprocessing import OneHotEncoder
import pandas as pd


class MultiColumnOneHotEncoder:
    def __init__(self):
        pass # array of column names to encode

    def fit(self, df):
        self.df = df
        self.subset = []
        self.df1=self.df.copy(deep=True)
        for col in self.df.columns:
            if self.df[col].dtype.name == 'object':
                self.subset.append(col)
                self.df = self.df.drop([col], axis=1)
        return self # not relevant here

    def transform(self):


        ohe = OneHotEncoder(categories='auto')
        feature_arr = ohe.fit_transform(self.df1[self.subset]).toarray()
        feature_labels = ohe.categories_
        feature_labels = np.array(feature_labels).ravel()
        features = pd.DataFrame(feature_arr, columns=feature_labels)
        result = pd.concat([self.df, features], axis=1, join='inner')
        return result
        


    def fit_transform(self,df):
        self.fit(df)
        return self.transform()


