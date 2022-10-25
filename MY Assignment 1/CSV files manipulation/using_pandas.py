import pandas

# data=pandas.read_csv('emp_bday.txt')
# data=pandas.read_csv('emp_bday.txt',index_col='name')
data=pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(data)
# print(type(data['department'][0]))

