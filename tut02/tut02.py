from typing import List, NewType

# Function to check whether input is valid or not
def isValid(input_nums):
    result=list()
    for x in input_nums:
        if(isinstance(x,int)==False):
            result.append(x)
    return result

# Function to calculate score
def get_memory_score(input_nums):    
    # Checking if input is valid or not
    result=isValid(input_nums)
    if(len(result)!=0):
        print("Please enter a valid input list")
        print("Invalid inputs detected:",result)
        exit()
    
    # Implementation of score calculator
    score=0
    temp=list()
    length=len(input_nums)
    for x in input_nums:
        check=1
        for y in temp:
            if(x==y):
                score+=1
                check=0
                break
        if(check):
            if(len(temp)==5):
                temp.pop(0)
            temp.append(x)
    return score

#Assign input_nums here
input_nums=[7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]

# Calling get_memory_score function
print("Score:",get_memory_score(input_nums))