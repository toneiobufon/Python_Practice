"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.
Examples:
- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)
Notes:
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Your code here
    # nested for loops/ brute force approach
    #outer loop loops over elements in nums
        #inner loop loops over the numbers in front of the outer loop
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]

    #ANOTHER APPROACH TO SOLVE
    #using a dictionary
    dict = {} #create empty dictionary

    # loop over the list of nums to populate dictionary
    for i in range(len(nums)): #O(n)
        dict[nums[i]] = i #O(1)

    #loop over list of nums
    for i in range(len(nums)):#O(n)

        #check if target-nums[i] is in dict, and that such number has not been used
        complement = target - nums[i] #O(1)
        if complement in dict and dict[complement] != i:

            return [i, dict[target-nums[i]]]
    
    return "No solution found" 


nums = [0,2,3,4,9]
target= 2

print(two_sum(nums, target))


##################################################################################################
"""
Demonstration #2
Given a non-empty array of integers `nums`, every element appears twice 
except for one. Write a function that finds the element that only appears once.
Examples:
- single_number([3,3,2]) -> 1
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
   
    if nums.count(x) == 1:
        return x


print(single_number([3,3,2]))