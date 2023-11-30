import pandas as pd 
class Buyssead: 

    def addMyFuture(self, my_future_dataframe): 

        my_info = { 

        'Name': ['Abby Buysse'], 

        'Major': ['IS and Marketing'], 

        'DesiredPosition': ['Insurance Underwriter'] 

            } 

        abby_df = pd.DataFrame(my_info) 

        updated_df = pd.concat([my_future_dataframe, abby_df]) 

 
 

        return updated_df 