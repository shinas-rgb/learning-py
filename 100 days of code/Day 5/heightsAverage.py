student_heights = [165, 167, 159, 170, 165, 168]
num_of_students = 0
sum_of_heights = 0

for height in student_heights:
    sum_of_heights += height
    num_of_students += 1

average_height = round(sum_of_heights / num_of_students, 2)
print(f"Average height of students: {average_height}")