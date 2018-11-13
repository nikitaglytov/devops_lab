movepath = input("Please enter commands to robot:")
commands = ('R', 'L', 'U', 'D')
x = 0
y = 0
for i in range(len(movepath)):
    if(movepath[i:i + 1:1] not in commands):
        print("Incorrect command found")
    if movepath[i:i + 1:1] == 'U':
        y += 1
    if movepath[i:i + 1:1] == 'D':
        y -= 1
    if movepath[i:i + 1:1] == 'R':
        x += 1
    if movepath[i:i + 1:1] == 'L':
        x -= 1

print('True' if (x == 0 and y == 0) else 'False')
