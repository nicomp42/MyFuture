#le2dc

import pandas as pd

class Le2dc:
    def addMyFuture(self, dataframe):
        # Perform operations on the DataFrame (for example, adding a new column)
        new_row = {
            'Name': 'Duc Nam Le',
            'Major': 'Business',
            'DesiredPosition': 'Marketing Specialist'
        }
        dataframe = dataframe._append(new_row, ignore_index=True)
        # Appending the new row to the DataFrame
    
        return dataframe

