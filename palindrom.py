import time
str1=input("Enter the string")
if(str1==str1[::-1]):
    print(str1,str1[::-1],":It is a Palindrom string")
else: 
    print(str1,str1[::-1],":It is not Palindrom string")
print()
time.sleep(2)
print("End of an application")       