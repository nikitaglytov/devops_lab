N = input("Please enter the number of students: ")
list1 = []
for i in range(int(N)):
    n = input("Name of {number} student: ".format(number=i + 1))
    M = input("Math marks: ".format(number=i + 1))
    Ph = input("Physics marks: ".format(number=i + 1))
    Ch = input("Chemistry marks: ".format(number=i + 1))
    list1.append({'n': n, 'M': float(M), 'Ph': float(Ph), 'Ch': float(Ch)})
find_name = input("Find name of student:")
for i in range(int(N)):
    if list1[i]['n'] == find_name:
        print((list1[i]['M'] + list1[i]['Ph'] + list1[i]['Ch']) / 3)
