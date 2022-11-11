import pandas as pd

class Adaptee():

    def csv_parse(self, file):
        Dataframe = pd.read_csv(file)
        
        return(Dataframe)
