# studentPackage/smith6kg

class Smith6kg:
    @staticmethod
    def addMyFuture(my_future_dataframe):
        # Adding a new row to the DataFrame
        new_row = {'Name': 'Keegan Smith', 'Major': 'IS/Comm', 'DesiredPosition': 'Developer'}
        my_future_dataframe = my_future_dataframe._append(new_row, ignore_index=True)
        return my_future_dataframe