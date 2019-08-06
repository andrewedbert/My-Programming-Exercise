import csv
students = []
with open('test.csv','r') as myfile:
    reader = csv.reader(myfile)
    # print(reader)
    for x in reader:
        print(x[0])
        students.append(x[0])
print(students)