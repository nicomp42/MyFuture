# studentPackage

class Liu4j4:
    def addMyFuture(self, dataframe):
        
        new_row = {'Name':'Johnny Liu', 
                   'Major':'Information Systems', 
                   'DesiredPosition':'Data Analyst'}
        myFuture = dataframe._append(new_row, ignore_index=True)
        return myFuture