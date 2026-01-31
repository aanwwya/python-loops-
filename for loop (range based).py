# FOR LOOP BAISC, RANGE BASED 


#1. print numbs from 1-10 
for num in range(1,11):
    print(num)

    
#2. print numbs from 10 to 1
for i in range(10,0,-1): #start = 10, stop val = 0, step val = -1
    print(i)  #i wil take values: 10,9,8,7..1 

    
#3. print even numbers between 1 and 20 
for num in range(1,21):
    if num % 2 == 0: #checks if num is divisible by 2 
        print(num) 


# alternative range based method for ques 3. 
for num in range(2,21,2):
    print(num)


#4. print odd numbs between 1 and 20 
for num in range(1,21):
    if num % 2 != 0: #between 1 and 20, when remainder is not equal to 0, print. 
        print(num) 

        
#5. print multiples of 5 up to 50
for num in range(1,51):
    if num % 5 == 0: 
        print(num)
         

# alternate method for ques 5. 
for num in range(5,51,5):
    print(num)
        

#6. print numbers from 0 to 50 with step 5
for num in range(0,51,5):
    print(num)
    
        
#7. print numbers from 100 to 0 with step -10
for num in range(100,-1,-10):
    print(num)
    

#8. print first 10 natural numbers 
for num in range(1,11):
    print(num)
    
    
#9. print numbers from 5 to 15 
for num in range(5,16):
    print(num) 
    

#10. print numbs from 20 to 30 
for num in range(20,31):
    print(num) 
    
    
#11. print numbs from 50 to 60 
for num in range(50,61):
    print(num) 
    

#12. print numbs from 15 to 5
for nums in range(15,4,-1):
    print(nums)
    
    
#13. print numbs from 30 to 10 with step -2
for nums in range(30,9,-2):
    print(nums) 
    
    
#14. print even nums between 10 and 40 
for nums in range(10,41):
   if nums % 2 == 0:
       print(nums)
       
       
#15. print even nums between 10 and 40 
for nums in range(10,41):
    if nums % 2 == 0:
        print(nums)
        
 
#16. print odd numbs between 25 and 50 
for nums in range(25,51):
    if nums % 2 != 0:
        print(nums) 
        
        
#alternate method for ques 16. 
for nums in range(25,51,2):
    print(nums)
    
        
#17. print numbs from 0 to 100 with step 20 
for nums in range(0,101,20):
    print(nums)
       

#18. print numbs from 1 to 50 with step 3
for nums in range(1,51,3):
    print(nums)
    
    
#19. print nums from 200 to 100 with step -25
for nums in range(200,99,-25):
    print(nums)
    
    
#20. print multiples of 7 between 1 to 70 
for nums in range(1,71):
    if nums % 7 == 0:
        print(nums)
        
        
#21. print multiples of 3 upto 30
for nums in range(1,31):
    if nums % 3 == 0:
        print(nums)
        