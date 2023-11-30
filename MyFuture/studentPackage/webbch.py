#webbch.py

import pandas as pd

class Webbch:
    def addMyFuture (self,dataframe):
        dataframe = dataframe._append({'Name': 'Charles Webb', 'Major': 'IS', 'DesiredPosition': 'Who Knows' }, ignore_index=True)
        return dataframe
    
if __name__ == "__main__":
    import pandas as pd
    
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
    #creating instance of webbch
    webbch = Webbch()
    my_future_dataframe = webbch.addMyFuture(my_future_dataframe)
    
    print(my_future_dataframe)
