import time
p1=input('Enter the password:')
p2=input("Enter the confirm password:")
print()
if p1==p2:
    print(p1,p2,":Password is valid")
else:
    print("Invalid password")
print()
time.sleep(2)
print("End of an application")        
