import csv
from typing import List, Dict
class HandleCSV:
    '''
    Different techniques to use the data in csv format.
    '''
    filename = "C:\\Users\\Anuja\\PycharmProjects\\HRconnect\\employees.csv"

    @classmethod
    def read_entire_csv(cls) -> List[Dict]:
        """
        Reads the data of each line in dict format
        :return: a list of dictionaries containing data of each line
        """
        entire = []
        with open(cls.filename, "r") as file:
            for line in csv.DictReader(file):
                entire.append(line)
        return entire

    @classmethod
    def read_csv_line_by_line(cls):
        """
        Reads the data line by line in dict format
        :return: each line in a dict format
        """
        with open(cls.filename) as bar:
            for line in csv.DictReader(bar):
                yield line
