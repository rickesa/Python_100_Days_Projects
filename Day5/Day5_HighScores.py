# Input a list of student scores. Return the highest score without using Max(), using a for loop
student_scores = [78,65,89,86,55,91,64,89]

# Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"the highest score in the class is: {high_score}")