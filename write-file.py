f=open("sample.txt","w")

f.write("I am learning Python.\n")
f.write("I am enjoying it.\n")
f.write("I am loving it.\n")
f.write("I am practicing it.\n")
f.close()

#jodi file er sheshe notun content add korte chai tahole "a" mode use korte hobe

f=open("sample.txt","a")
f.write("I am going to be a good programmer.\n")
f.write("I am going to be a good developer.\n")
f.close()

with open("sample.txt","r") as f:
    data=f.read()
    print(data)