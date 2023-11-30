#create a class using 6+2 capitalize the first letter
#add a function that says addMyFuture
#place it in studentpackage and call it your 6+2
import pandas as pd
class Teklemka:
    def addMyFuture(self, dataframe):
        data = {
            'Name': ['Kirubel Teklemariam'],
            'Major': ['Information Systems'],
            'DesiredPosition': ['Data Engineer']
        }
    

        dataframe = dataframe._append(data, ignore_index=True)
        # Appending the new row to the DataFrame
    
        return dataframe