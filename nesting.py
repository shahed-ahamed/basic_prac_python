age = int(input("Enter your age: "))

if (age >= 18):
    if (age < 65):
        print ("You are eligible to work")
    else:
        print ("You are retired")
else:
    print ("You are not eligible to work")       