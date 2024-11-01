#BMI checker

height=int(input("height=")) 
weight=int(input("width="))

bmi =weight/(height/100)**2
if bmi<=18.4:
    print("you are underweight",bmi)
elif bmi<=34.9:
   print("you are over weight",bmi)
elif bmi<=24.9:
    print("you are healthy",bmi)
else:
    print("you are obese")