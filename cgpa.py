user_input=float(input("Enter your cgpa:"))
if user_input >= 4.0 and user_input >= 3.7:
    print("Your grade is A+")
elif user_input < 3.7 and user_input >= 3.5:
    print("Your grade is A")
elif user_input < 3.5 and user_input >= 3.0:
    print("Your grade is B")
elif user_input < 3.0 and user_input >= 2.5:
    print("Your grade is C")
else:
    print("Sorry you are fail")                