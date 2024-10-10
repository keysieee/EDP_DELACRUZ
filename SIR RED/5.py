students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]

highest_student = students_scores[0][0]  
highest_score = students_scores[0][1]    

for i in range(1, len(students_scores)):  
    if students_scores[i][1] > highest_score:
        highest_student = students_scores[i][0]
        highest_score = students_scores[i][1]

print("The student with the highest score is:", highest_student, "with a score of", highest_score)