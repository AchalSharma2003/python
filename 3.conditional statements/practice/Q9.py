"""Q9: Take a student's marks as input. Print their grade based on this scale:
90 and above →A
75 to 89 →B
60 to 74 →C
40 to 59 →D
Below 40 →F
 """


percentage =int(input("enter the percentage : "))

if percentage>=90 and percentage<=100:
    print("A grade")
elif percentage>=75 and percentage<=89:
    print("B grade")
elif percentage>=60 and percentage<=74:
    print("C grade")
elif percentage>=40 and percentage<=59:
    print("D grade")
elif percentage >=0 and percentage<=39:
    print("fail") 
else:
    print("invalid percentage")
