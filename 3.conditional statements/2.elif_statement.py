percentage =int(input("enter the percentage : "))

if percentage>=91 and percentage<=100:
    print("A grade")
elif percentage>=81 and percentage<=90:
    print("B grade")
elif percentage>=71 and percentage<=80:
    print("C grade")
elif percentage>=61 and percentage<=70:
    print("D grade")
elif percentage >=0 and percentage<=60:
    print("fail") 
else:
    print("invalid percentage")
