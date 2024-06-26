def calculate_average_marks(data):

    total_marks = 0

    num_students = 0

    

    for student in data:

        if 'MARKS' in student:

            total_marks += int(student['MARKS'])

            num_students += 1

    

    if num_students == 0:

        return 0

    

    return total_marks / num_students



# Read input

N = int(input())

columns = input().split()



# Initialize data structure to store student records

students = []



# Read student data

for _ in range(N):

    student_data = input().split()

    student_record = {columns[i]: student_data[i] for i in range(len(columns))}

    students.append(student_record)



# Calculate average marks

average_marks = calculate_average_marks(students)



# Print average marks with two decimal places

print("{:.2f}".format(average_marks))
