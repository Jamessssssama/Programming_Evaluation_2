#input marks
first_mark = float(input("Enter your first course mark:"))
second_mark = float(input("Enter your second course mark:"))
third_mark = float(input("Enter your third course mark:"))
fourth_mark = float(input("Enter your fourth course mark:"))
average = round((first_mark + second_mark + third_mark + fourth_mark) / 4, 2)
grade = "TBD"

#determine grades
if average >= 95 and average <= 100:
  grade = "A+"

elif average >= 87 and average < 95:
  grade = "A"

elif average >= 80 and average < 87:
  grade = "A-"

elif average >= 77 and average < 80:
  grade = "B+"

elif average >= 72 and average < 77:
  grade = "B"

elif average >= 70 and average < 72:
  grade = "B-"

elif average >= 67 and average < 70:
  grade = "C+"

elif average >= 63 and average < 67:
  grade = "C"

elif average >= 60 and average < 63:
  grade = "C-"

elif average >= 57 and average < 60:
  grade = "D+"

elif average >= 54 and average < 57:
  grade = "D"

elif average >= 50 and average < 5:
  grade = "D-"

elif average >= 0 and average < 50:
  grade = "F"

else:
  grade = "/"
  average = "/"
  print("error")

#print the output mark and score
print("The average is", average, "% and your grade is", grade)
