import csv

with open('new_emp.txt',mode='w') as csv_file:
    emp_writer=csv.writer(csv_file, delimiter=',')
    emp_writer.writerow(['John Smith','Accounting','March'])
    emp_writer.writerow(['Erica Rode','IT','April'])