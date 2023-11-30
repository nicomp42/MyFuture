# create a class using your 6+2 and capitalize the first letter 
# write a method in the class called Add my future
# he will pass a dataframe we add and row and then we pass it back to him
# put code in the student package and call it rodenky.py
# when you get code working do commit and push 

import pandas as pd


class Rodenky:
    def addMyfuture (self, my_future_dataframe):
        # Adding a new row to the dataframe
        new_row = {
            'Name':'Kelly Roden', 
            'Major': 'Economics/Finance', 
            'DesiredPosition': 'IT Auditor'
            }
        my_future_dataframe = my_future_dataframe._append(new_row, ignore_index=True)
        # Appending the new row to the dataframe
        return my_future_dataframe


