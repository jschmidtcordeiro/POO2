from parse import IParse
from adaptee import Adaptee

class Adapter(IParse):
    __adaptee = Adaptee()

    def parse(self, file) -> dict:
        Dataframe = self.__adaptee.csv_parse(file)
        columns = Dataframe.columns
        json = {}
        i = 0
        while i < len(columns):
            json[columns[i]] = columns[i + 1]
            i += 2
        return json