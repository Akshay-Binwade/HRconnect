from my_utils.csv1 import HandleCSV
from datetime import datetime

'''
Gives dictionary of hire date vs list of employees name whose dept id is between 30-110 and salary above 4200.
'''

if __name__ == '__main__':
    d = {}
    for i in HandleCSV.read_csv_line_by_line():
        if int(i["DEPARTMENT_ID"]) in range(30, 111) and (int(i["SALARY"]) > 4200):
            b = datetime.strptime(i["HIRE_DATE"], "%d-%b-%y")
            f = (i["FIRST_NAME"]), (i["LAST_NAME"])
            d.setdefault(str(b.date()), []).append(" ".join(f))
    print(d)