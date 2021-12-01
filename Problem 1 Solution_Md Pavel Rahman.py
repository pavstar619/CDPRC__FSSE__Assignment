employees = [
    ['1','Alice'],
    ['2','John'],
    ['3','Jane'],
    ['4','Alice'],
    ['5','Bob']
]

files = [
    ['100','jpeg'],
    ['Alice','png'],
    ['3','jpg'],
    ['1','jpg'],
    ['John','jpeg']
]

count = 0
alreadyRecorded = [] # unique file types will be appended in here.

for i in range(len(employees)):
    for j in range(len(files)):
        if employees[i][0] == files[j][0] or employees[i][1] == files[j][0] and files[j][1] not in alreadyRecorded:
            count+=1
            alreadyRecorded.append(files[j][1])
            break

print(f'Result: {count}')