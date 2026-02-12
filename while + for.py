# questions using both for and while 

#1. print numbers from 1-10
# usin while 
i = 1 #starting val
while i<=10: #condition
    print(i)
    i = i+1 #increment
    
# using for
for i in range(1,11): #start val = 1 stops at 10
    print(i) # i automatically takes val from 1-10, no increment 
  
    
    
#2. print numbers from 10-1
#using while 
i = 10  #start val 
while i>=1: 
    print(i)
    i = i-1 #decreases number each time by 1
    
#using for loop 
for i in range(10,0,-1):
    print(i)
    
    
#3. print even numbers from 1-20
# using while
i = 2 #start val 
while i<=20:
    print(i)
    i = i+2

#using for
for i in range(2,21,2):
    print(i)
    

#4. print odd numbers from 1 to 20
#using while loop
i = 1 # start val = 1 
while i<=20:
    print(i)
    i = i + 2 
# same logic as even nums, only start val changes 

#for loop
for i in range(1,21,2):
    print(i)


#5. print numbers from 1 to 100 with steps 5 
#using while 
i = 1
while i<=100:
    print(i)
    i = i + 5
    
# for loops:
for i in range(1,101,5):
    print(i)
    
    
#6. print multiplication table of 5 
#using while loop 
i = 1 
while i<=10:
    print("5 *", i, "=", 5*i)
    i = i+1
    
# using for 
for i in range(1,11):
    print("5 *", i, "=", 5*i)
    
    
#7. print numbers divisible by 3 from 1-30
# using while loop
i = 1 
while i<=30:
    if i % 3 == 0:
        print(i)
    i = i + 1
    
#using for loop:
for i in range(1,31):
    if i % 3 == 0:
        print (i)
        

#8. find sum of numbers from 1 to 10 
# using while 
i = 1
total = 0
while i<=10:
    total = total + i
    i = i + 1
print("sum = ", total)

# for loop 
total = 0 
for i in range(1,11):
    total = total + i
print("sum =", total)
    

#9. print squares of numbers from 1 - 10 
# using while 
i = 1
while i<=10:
    print(i*i)
    i = i+1

# for loop 
for i in range(1,11):
    print(i*i)
    

#10. print numbers until 20 but stop if numbers becomes 15 
# using while 
i = 1
while i<=20:
    if i == 15:
        break
    print(i)
    i = i + 1
    
# usin for loop 
for i in range(1,21):
    if i == 15:
        break
    print(i)

    

    
    