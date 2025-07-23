students_records = {}

while True:
    student_id = input("Enter student ID (or 'exit' to quit): ")
    if student_id.lower() == 'exit':
        break
    
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    
    students_records[student_id] = {
        'name': name,
        'age': age
    }