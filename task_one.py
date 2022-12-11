'''
Printing Name, email, phone no of employees having salary greater than 9000.
'''

from my_utils.csv1 import HandleCSV

if __name__ == '__main__':
    for i in HandleCSV.read_csv_line_by_line():
        d = {}
        if int(i["SALARY"])>9000:
            a =[i["FIRST_NAME"],i["LAST_NAME"]]
            d["Name"] = " ".join(a)
            d["Email"] = i["EMAIL"]
            d["Phone no"]= i["PHONE_NUMBER"].replace(".","")
            print(d)