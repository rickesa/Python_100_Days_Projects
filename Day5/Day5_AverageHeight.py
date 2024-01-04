student_heights = [156,178, 165, 171, 187]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
count_students = 0
# print(student_heights[0])
for height in student_heights:
    total_height += height
    print(total_height)
    count_students += 1

# for student in range(0, len(student_heights)):
#     total_height += student_heights[student]
#     count_students += 1

average_height = round(total_height / count_students)
print(f"average height = {average_height}")