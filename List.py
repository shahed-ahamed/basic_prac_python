marks1 = 94.4
marks2 = 89.5
marks3 = 78.9
marks4 = 99.0
marks5 = 85.6
marks6 = 79.5

#uporer gula ke ek sathe rakhte list use kora jay nicher niyomee
marks = [94.4, 89.5, 78.9, 99.0, 85.6, 79.5]
print(marks)
print(type(marks))

#jodi index print korte chai tahole
print(marks[0])  #first index
print(marks[1])  #second index
print(marks[2])  #third index

#amra python list er moddhe jekono dhoroner data (str,int,float) rakhte pari
data = [45, 67.8, 'Hello', True, 56, 'World']
print(data)

#string hocche immutable mane change kora jay na. kintu list hocche mutable mane change kora jay

#list hocche mutable tai amra list er moddhe notun element add korte pari or jekon element ke remove korte pari
#list er moddhe notun element add korar jonno amra append() method use kori


#list slicing o kora jay
print(data[0:4])  #first index theke 4 number index porjonto print korbe
print(data[2:])   #2 number index theke shob gulo print korbe
print(data[:4])   #first index theke 4 number index porjonto print korbe
print (data[2:4])
print (data[-1])  #last index print korbe
print (data[-1:-4])  #last index theke -4 index porjonto print korbe
print (data[-4:-1])  #-4 index theke last index porjonto print korbe



#______________________________________________________________________________________________________________________________
#List er kichu important method
#1. append() method: list er sheshe notun element add kore
data.append('Python')
print(data)

#sort() method: list er element gulo ke ascending order e sort kore
numbers = [45, 67, 23, 89, 12, 90]
numbers.sort()
print(numbers)

number.sort(reverse=True)  #descending order e sort korbe
print(numbers)