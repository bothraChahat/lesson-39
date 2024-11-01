#exam eligibilty
total_working_days =int(input( "Enter the total number of working days"))
days_absent =int(input( "Enter the total number of days absent"))

#calculate days attended and attendance percentage
days_attendance = total_working_days - days_absent
attendance_percentage =(days_attendance / total_working_days)*100

#check attendance eligibilty
if attendance_percentage >75:
    print("  you are eligible to sit in the exam")
else:
    print("  you are not eligible to sit in the exam")