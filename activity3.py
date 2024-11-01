num=int(input("enter a number"))

 
  #check whether it is even or odd
if num>50:
    print(num,"is greater than 50")
    if num%2==0:
      print("and the number is even")
    else:
      print("and the number is odd")
else:
    print(num,"is less than 50")