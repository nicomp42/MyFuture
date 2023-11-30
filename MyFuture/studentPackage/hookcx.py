
#create a class using your 6+2, capitalize first letter
#write method in that class called "add my future"
#pass data frame, add row to data frame, pass it back 
#student package called 6+2.py


import pandas as pd

class Hookcx:
    def addMyFuture(self, dataframe):
    # Adding a new row to the DataFrame
        new_row = {
            "Name":"Cassidy Hook",
            "Major":"IS/MKTG",
            "DesiredPosition":"Consultant"
        }
        dataframe = dataframe._append(new_row, ignore_index=True)
        #append new row to dataframe
        return dataframe
        
    
