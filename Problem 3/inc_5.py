"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name:
Lab Time:
"""

def inc_5():
    firstNum = int(input())
    secNum = int(input())
    nums = ""
        
    while secNum >= firstNum:
        nums += str(firstNum)
        firstNum += 5
        if firstNum <= secNum:
            nums += " "
        
        print(nums)


if __name__ == '__main__':
    inc_5()