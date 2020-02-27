students_DB={}
student_number=None
 
#ask input from user or 'q' to exit
while True:
    line = input('Please input the ID and name separated by comma or q to exit: ')
    if line == 'q':
        break
 
    id, name = line.split(',')
    students_DB.update({id:name})
 
#output

print(students_DB)