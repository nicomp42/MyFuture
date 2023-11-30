import pandas as pd
class Hamiltsw():
    def addMyFuture(self, df1):
        df2 = pd.DataFrame({
            'Name': ['Stewart Hamilton'],
            'Major': ['Information Systems'],
            'DesiredPosition': ['Software Developer']
        })
      
        return pd.concat([df1, df2], ignore_index=True)