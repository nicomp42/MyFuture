#GonzameClass 
import pandas as pd

class Gonzame:
    def addMyFuture(self, dataframe):
        # Adding new information to the DataFrame
        dataframe = dataframe._append({'Name': 'Michael Gonzales', 'Major': 'Information Systems', 'DesiredPosition': 'Software Developer'}, ignore_index=True)
        return dataframe

if __name__ == "__main__":
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
    # Creating an instance of Gonzame
    gonzame = Gonzame()
    
    # Adding new information to the DataFrame using Gonzame
    my_future_dataframe = gonzame.addMyFuture(my_future_dataframe)
    
    # Displaying the updated DataFrame
    print(my_future_dataframe)