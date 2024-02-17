#A student will not be allowed to sit in exam if there attendance is less than 75% check there attendance and give output accordingly

#Taking Input from User
classes_held=int(input("Total No. of Classes Held : ")) #No. of Classes Held
classes_attend=int(input("Total No. of Classes Attended : ")) #No. of Classes Attnended
attendance=(classes_attend/classes_held)*100 #Attendance Percentage
print("Your Attendance is : ",attendance,"%")

#Checking for mininum requirement a output accordingly
if attendance<75:
    print("You're not allowed to sit in the Exam.")
else:
    print("You're allowed to sit in the Exam.")