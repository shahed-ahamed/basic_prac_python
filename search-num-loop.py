# question : search a number in a list using loop

nums = [12,45,67,89,23,90,11,34,56,78]
n = int(input("Enter a number to search: "))

i=0 #initialize index

while i < len(nums):
    if (nums[i] == n):
        print(f"{n} is found at index {i}")
        break
    i+=1  
    
