#
import pandas as pd

class Fletchax():
    def addMyFuture(self, dataFrame):
        dataFletchax = {
            'Name': ['Alexander Fletcher'],
            'Major': ['Accounting & Information Systems'],
            'DesiredPosition': ['Marketing Manager']
        }
        
        fletchaxFuture = pd.DataFrame(dataFletchax)
        addRow = pd.concat([dataFrame,fletchaxFuture])

        return addRow