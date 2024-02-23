"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:
Lab Time:
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE
    x = -10
    y = -10
    not_found = True
    while x < 11 and not_found:
        while y < 11 and not_found:
            eq1 = a * x + b * y
            eq2 = d * x + e * y
            if eq1 != c or eq2 != f:
                y += 1
            else:
                print(f"x = {x} , y = {y}")
                not_found = False
    
    if not_found:
        print("There is no solution")
                        
    
    
if __name__ == "__main__":
    brute_eq()