#1. print numbers from 1-10 using a loop 
for num in range(1,11):
    print(num)
    
#2. calculate the sum of numbers from 1-10 using a loop 
sum_numbers = 0 
for num in range(1,11):
    sum_numbers = sum_numbers + num
print(sum_numbers) 

#3. print the elements of a list using a for loop 
my_list = [1,2,3,4,5]
for element in my_list:
    print (element)
    
#4. calulate the prod of elements in a list using a for loop
my_list = [2,3,4,5]
product = 1 
for num in my_list:
    product = product * num 
print(product) 

#5. print numbers from 1-10. if a num is even, break the loop using a for loop and else clause:
for num in range(1,11):
    if num % 2 == 0:
        break 
    print(num)
else:
    print("loop completed successfully")
    
#6. print numbers from 1 to 10. 
# if a number is even, skip it using a for loop and else clause:

for num in range(1, 11):
    if num % 2 == 0:
        continue  #har even num skip hoga 
    print(num)
else:
    print("loop completed successfully") 
    
# continue does not stop the loop so else still runs

#7. print nums from 1-10. if a num is divisible by 4, stop the loop using a for loop and break statement 
for num in range(1,11):
    print(num)
    if num % 4 == 0:
        break 
#break 4 pe stop kar dega, num 5-10 kabhi reach he nahi hoga 

#8. print numbers from 1-5, except 3 using a for loop and continue statement:
for num in range(1,6):
    if num == 3:
        continue 
    print(num)  #num = 3 pe continue execute hoga and 3 print nahi hoga 

#9. print numbers in a list until a negtive number is encountered using a while loop 
#  index based while loop 
my_list = [1,4,6,8,10,-3,5,7]
index = 0 
while my_list[index] >=0:
    print(my_list[index])
    index +=1  
# 10 tak print hoga and not -3 
#loop continues until a negative num is encountered, the negative num itself is not printed 

#10. find the common elements in two lists using a for loop 
#common elements leke ek third list mein store kiya
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
common_elements = []
for element in list1:  #take one value at a time from list1 & store it in variable element, loop 5 baar run hoga 
    if element in list2:
        common_elements.append(element)
    print(common_elements) # print is inside the for loop so it runs every iteration not once at the end 

    