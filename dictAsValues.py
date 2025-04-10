'''
Dictionary - made up of Key/Value pairs
A Key's value can be: int, str, float, boolean, LIST, DICTIONARY
'''

students = {}
num_students = int(input("Enter the total number of students: "))

# Student's name (first name)
# Student's Home School
# Student's Age
# Student's Town

'''
What you don't want to do: 

students = {'name': 'Hunter', 'chool': 'Canton', 'Age': 17, 'Town': 'Canton', 'name': } - key's have to be unique

Instead associate the one common element with an nested dictionary as that elements value
'''

for student in range(num_students):
    print("\nStudent", student + 1, ': \n')
    name = input("Enter the student's first name: ")
    school = input("Enter the student's school: ")
    age = input("Enter the students's age: ")
    town = input("Enter the student's town: ")

    # Store the data in the dictionary
    # the name variable as our key, and create a dictionary of the other variable keys/values as its value
    students[name] = {
        'School': school,
        'Age': age,
        'Town': town
    }

print(students)

'''
task -> Key for the dictionary
task1, task2, task3,  
'''