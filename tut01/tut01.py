"""This will detect meraki numner"""
def meraki_helper(n):
    prev=n%10+1
    original=n
    while(n):
        if(abs((n%10)-prev)!=1):
            return False
        prev=n%10
        n=n//10  
    return True

"""This function performs input/output operation"""
def main():
    inp=[12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
    size=len(inp)
    i=0
    meraki = 0
    non_meraki = 0
    while(i<size):
        temp = inp[i]
        if(meraki_helper(temp)):
            print("Yes -",temp,"is a Meraki number")
            meraki += 1
        else:
            print("No -",temp,"is not a Meraki number")
            non_meraki += 1
        i+=1
    print("the input list contains",meraki," meraki and",non_meraki,"non meraki numbers.")

"""Calling main function"""
main()