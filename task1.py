N = input("Please enter the number of students: ")
list1 = []
for i in range(int(N)):
    Name = input("Name of {number} student: ".format(number=i + 1))
    Math = input("Mark of Math for {number} student: ".format(number=i + 1))
    Physics = input("Mark of Physics for {number} student: ".format(number=i + 1))
    Chemistry = input("Mark of Chemistry for {number} student: ".format(number=i + 1))
    list1.append({'Name': Name, 'Math': float(Math)})
    list1.append({'Physics': float(Physics), 'Chemistry': float(Chemistry)})
find_name = input("Find name of student:")
for i in range(int(N)):
    if (list1[i]['Name'] == find_name):
        print((list1[i]['Math'] + list1[i]['Physics'] + list1[i]['Chemistry']) / 3)
