# for loop (index based)

#1. print all elements using index 
nums = [ 10,20,30,40,50]
for i in range(len(nums)): #len(nums) gives no of elements in the list 
    print(nums[i]) # give the element at index i in the list nums
    
    
#2.print index and element together 
# index based traversal
nums = [10,20,30,40,50]
for i in range(len(nums)):
 print(i,nums[i])
    
    
#3. print elements at even index 

#method 1: using condition 
nums = [10,20,30,40,50]
for i in range(len(nums)):
    if i % 2 == 0:
        print(nums[i])

#method 2: using step value 
for i in range(0,len(nums), 2):
    print(nums[i])


#4. print elements at odd index 
nums = [10,20,30,40,50]
for i in range(len(nums)):
    if i % 2 != 0:
        print(nums[i])
        

#5. reverse listt using loops

#method 1: reverse printing without new list 
nums = [10,20,30,40,50]
for i in range(len(nums)-1,-1,-1):
    print(nums[i])
    
#method 2: store reversed list 
nums = [ 10,20,30,40,50]
rev = []
for i in range(len(nums)-1,-1,-1):
    rev.append(nums[i])
print(rev)


#6. print elements at index multiple of 3
nums = [5,12,7,20,9,3]
for i in range(len(nums)):
    if i % 3 == 0:
        print(nums[i])
        

#7. print sum of elements at even index
nums = [5,12,7,20,9,3]
total = 0 
for i in range(len(nums)):
    if i % 2 == 0:
        total = total + nums[i]
print(total)


#8. count elements at odd index 
nums = [5, 12, 7, 20, 9, 3]
count = 0
for i in range(len(nums)):
    if i % 2 != 0:
        count = count + 1 
print(count)


#9. print elements greater than previous element (index comparision)
nums = [5, 12, 7, 20, 9, 3]
for i in range(1,len(nums)):
    if nums [i]> nums[i-1]:
        print(nums[i])
        
        
#10. replace elements at even index with 0 
nums = [5,12,7,20,9,3]
for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = 0
print(nums)


#11. print first and last element using index
nums = [8,3,15,6,9,12,4]
print(nums[0])
print(nums[len(nums) - 1])


#12. print index elements between 2 and 5 (inclusive)
nums = [8,3,15,6,9,12,4]
for i in range(2,6):
    print(nums[i])
    

#13. print element and its index in reverse order 
nums = [4,9,2,7,5,1,8]
for i in range(len(nums)-1,-1,-1):
    print(i,nums[i])
    
    
#14. find max element using index(no max)
nums = [8,3,15,6,9,12,4]
max_val = nums[0]
for i in range(1,len(nums)):
    if nums[i]>max_val:
        max_val = nums[i]
print(max_val)


#15.swap first and last element using index 
nums = [8,3,15,6,9,12,4]
temp = nums[0] #temp = 8 
nums[0] = nums[len(nums)-1]  #[len(nums)-1] = cause indexing starts from 0 
nums[len(nums) - 1] = temp
print(nums) 
#last index  = length -1, nums[6] = 4






    






