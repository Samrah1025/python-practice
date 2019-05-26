sub1=int(input("Enter marks of the biology subject: "))
sub2=int(input("Enter marks of the chemistry subject: "))
sub3=int(input("Enter marks of the english subject: "))
sub4=int(input("Enter marks of the pak.studies subject: "))
sub5=int(input("Enter marks of the sindhi subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80):
    print("Grade: B")
elif(avg>=70):
    print("Grade: C")
elif(avg>=60):
    print("Grade: D")
else:
    print("Grade: F")