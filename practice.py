# import csv
#
# with open("employees.csv",newline="") as file:
#     data = csv.DictReader(file)
#
#     with open("newfile2.csv","w") as file2:
#         fieldnames = ("FIRST_NAME", 'LAST_NAME', 'EMAIL','PHONE_NUMBER', 'SALARY', 'DEPARTMENT_ID', 'COMMISSION_PCT', 'JOB_ID', 'EMPLOYEE_ID', 'HIRE_DATE', 'MANAGER_ID')
#         data2 = csv.DictWriter(file2, fieldnames=fieldnames)
#         data2.writeheader()
#         for l in data:
#             data2.writerow(l)
#
#
# # with open("employees.csv", newline="") as file:
# #     data = csv.reader(file)
# #     i=0
# #     for j in data:
# #         print(j)
# #         if i==0:
# #             fieldname = j
# #         i+=1
# #     print("Fieldname: ",fieldname)
# #     print(data)

import csv

# with open("employees.csv",newline="") as file:
#     a = csv.DictReader(file)
#     d = {}
#     for i in a:
#         # if 30 < int(i["DEPARTMENT_ID"]) < 111:
#         #     if int(i["SALARY"])>4200:
#         if int(i["DEPARTMENT_ID"]) in range(30,111) and (int(i["SALARY"])>4200):
#                 b = datetime.strptime(i["HIRE_DATE"],"%d-%b-%y")
#                 f = (i["FIRST_NAME"]), (i["LAST_NAME"])
#                 d.setdefault(str(b.date()),[]).append(" ".join(f))
#     print(d)


from my_utils.csv1 import HandleCSV
from datetime import datetime
d = {}
for i in HandleCSV.read_csv_line_by_line():
    if int(i["DEPARTMENT_ID"]) in range(30, 111) and (int(i["SALARY"]) > 4200):
        b = datetime.strptime(i["HIRE_DATE"], "%d-%b-%y")
        f = (i["FIRST_NAME"]), (i["LAST_NAME"])
        d.setdefault(str(b.date()), []).append(" ".join(f))
print(d)

