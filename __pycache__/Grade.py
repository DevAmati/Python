#prompt to input marks
mark1 = int(input("Enter marks for the first subject"))
mark2 = int(input("Enter the marks for the second subject"))
mark3 = int(input("Enter mark for the third subject"))
#formula for average
average = (mark1 + mark2 + mark3)/3
if average >=70 and average <= 100:
    print (" Grade A")
elif average >=60 and average <=69:
    print ("Grade B")
elif average >=50 and average <=59:
    print("Grade c")
elif average >= 40 and average <=49:
    print("Grade D")
elif average >= 0 and average <=39:
    print ("Fail")
else:
     print ( "Inavalid value")

        