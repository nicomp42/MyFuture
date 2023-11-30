    
import pandas as pd

class Smith6mx:
    def addMyFuture(self, dataframe):
        smith6mx_data = {
            'Name': ['Max Smith'],
            'Major': ['Information Systems and Mathematics'],
            'DesiredPosition': ['Data Architect']
        }
        smith6mx_df = pd.DataFrame(smith6mx_data)
        dataframe = pd.concat([dataframe, smith6mx_df], ignore_index=True)
        return dataframe


smith6mx = Smith6mx()
