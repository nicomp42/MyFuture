#Waltemw.py
import pandas as pd


class Waltemw:
    def addMyFuture(self, dataframe):
        # Data for the DataFrame
        mydata = {
            'Name': ['Matt Walters'],
            'Major': ['Information Systems'],
            'DesiredPosition': ['Data Analyst']
        }
    
        dataframe = dataframe._append(mydata, ignore_index=True)
        # Appending the new row to the DataFrame

        return dataframe

