import csv

# students = {
#     'ID 1': {'Name': 'Shaun', 'Age': 35, 'City': 'Delhi'},
#     'ID 2': {'Name': 'Ritika', 'Age': 31, 'City': 'Mumbai'},
#     'ID 3': {'Name': 'Smriti', 'Age': 33, 'City': 'Sydney'},
#     'ID 4': {'Name': 'Jacob', 'Age': 23, 'City': 'Pune'},
#}

data = {
    "ID": [101, 102, 103],
    "Name": ["Anjana", "Prateek", "Steffi"],
    "Job": ["Developer", "Engineer", "Doctor"],
    "Salary": [20000, 30000, 15000],
}
with open('/home/my/Downloads/output.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow(data.keys())
    writer.he
    for i in data.values():
        writer.writerows([i])



#
# import pandas as pd
#
# student = [{"Name": "Vishvajit Rao", "age": 23, "Occupation": "Developer","Skills": "Python"},
# {"Name": "John", "age": 33, "Occupation": "Front End Developer","Skills": "Angular"},
# {"Name": "Harshita", "age": 21, "Occupation": "Tester","Skills": "Selenium"},
# {"Name": "Mohak", "age": 30, "Occupation": "Full Stack","Skills": "Python, React and MySQL"}]
#
# # convert into dataframe
# df = pd.DataFrame(data=student)
#
# #convert into excel
# df.to_excel("/home/my/Downloads/students.xlsx", index=False)
# print("Dictionary converted into excel...")
