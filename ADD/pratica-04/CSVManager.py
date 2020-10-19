import pandas as pd
import numpy as np


class CSVManager:
    def read(self, filePath):
        return pd.read_csv(filePath)

    def deleteClass(self, df):
        return df.drop(columns=['class'])

    def convertMatrixToCSV(self, mat):
        csvMatrix = np.asarray(mat)
        return csvMatrix

    def writeCSV(self, csv, path):
        np.savetxt(path, csv, delimiter=",", fmt="%10.5f")

    def replaceNan(self,df,cols_with_missing):

        for i in cols_with_missing:
            if type(df[i][0]) != str:
                df[i].fillna(df[i].mean(),inplace=True)
            else:
                df[i].fillna('No-Value',inplace=True)
            
        return df