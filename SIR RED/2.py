students = ('John', 'Maria', 'David', 'Samantha')

index = 2  

if index < len(students):  
    count = 0
    for student in students:
        if count == index:
            print(student)
            break
        count += 1
else:
    print("Index out of range")