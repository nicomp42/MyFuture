# cruzbm.py 
import pandas as pd 
class Cruzbm: 
    def addMyFuture(self,dtafrm):
        '''
        @param: dtafrm-- dataframe you want to append to 
        @return: adds information to dataframe
        '''
        data = {
            'Name': ['Brianna Cruz'],
            'Major': ['Information Systems'],
            'DesiredPosition': ['Business Intelligence Analyst']
        }
        
        myFuture = pd.DataFrame(data)
        
        appended = pd.concat([dtafrm,myFuture])
        
        return appended 