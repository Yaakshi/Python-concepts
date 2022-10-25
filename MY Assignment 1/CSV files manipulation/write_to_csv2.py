from asyncore import write
import csv

with open('new_emp2.txt', mode='w') as csv_file:
    fields=['empname','dept','birthmonth']
    emp_writer=csv.DictWriter(csv_file, fieldnames=fields)
    emp_writer.writeheader();
    emp_writer.writerow({'empname':'John','dept':'CSE','birthmonth':'April'})
    emp_writer.writerow({'empname':'Erica','dept':'ECE','birthmonth':'October'})