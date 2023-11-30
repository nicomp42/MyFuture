# main.py
# Do not edit this module!

import pandas as pd

# Bill will add import statements to bring in your classes
#from studentPackage.nicholdw import *

class ProjectDriver:
    def create(self):
        # Data for the DataFrame
        data = {
            'Name': ['John Doe', 'Jane Smith', 'Bob Johnson'],
            'Major': ['Computer Science', 'Engineering', 'Business'],
            'DesiredPosition': ['Software Developer', 'Mechanical Engineer', 'Marketing Manager']
        }

        # Creating a DataFrame
        myFuture = pd.DataFrame(data)

        return myFuture

# Example usage
project_driver = ProjectDriver()
my_future_dataframe = project_driver.create()

# Displaying the DataFrame
print(my_future_dataframe)

# Bill will add this code to invoke your method
#nicholdw = Nicholdw()
#my_future_dataframe = nicholdw.addMyFuture(my_future_dataframe)
#...




