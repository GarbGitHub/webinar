student_marks = [4, 3, 2, 3, 4]

# yaml
marks_sum = 0
for item in student_marks:  # next
    marks_sum += item

avg_mark = marks_sum / len(student_marks)
print(avg_mark)

