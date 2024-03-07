print ("Grades")
grade1=int(input("Enter grade1 : "))
grade2=int(input("Enter Grade2 : "))
grade3=int(input("Enter Grade3 : "))

sum=grade1+grade2+grade3
average=sum/3

print ("Total Grades =",sum)
print ("Average = ",average)

if average>=90:
    print("A Pass")
elif average>=80:
    print("B Pass")
elif average>=70:
    print("C Pass")
else:
    print("D Failed")
