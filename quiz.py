import random
while(True):
    try:
        type = int(input("Enter 1 for an addition problems, 2 for a subtraction problems"))
        

    except:
        print("Enter a valid Integer")

    if((type==1)or(type==2)):
        break

while(True):
    try:
        number = int(input("How many questions would you like in your quiz:"))
        

    except:
        print("Enter a valid Integer")

    if(number>0):
        break
    else:
        print("Enter a value greater than 0:")
n=0
while(n==0):
     try:
        diff = int(input("How difficult would you like your quiz"))
        n=1
     except:
        print("Enter a valid Integer")

correct =  0  
for i in range(0,number):
    lower = 1*(10**(diff-1))
    upper = 1*(10**diff)-1
   


    a = random.randint(lower, upper)
    b = random.randint(lower, upper)

    if(type==1):
        c = a+b
        count = 0
        
        print(a,"+",b)
        while(True):
            count+=1
            answer = int(input("Give Answer"))
            if(answer==c):
                break
            else:
                print("Enter Correct Answer")
        if(count==1):
            correct+=1
    if(type==2):
        if(a>b):
            c = a-b
            print(a,"-",b)
        else:
            c= b-a
            print(b,"-",a)
        count = 0
        
       
        while(True):
            count+=1
            answer = int(input("Give Answer"))
            if(answer==c):
                break
            else:
                print("Enter Correct Answer")
        if(count==1):
            correct+=1
print((correct/number)*100)


            
            
