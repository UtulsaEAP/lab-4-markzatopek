"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Mark Zatopek 
Lab Time: Thurs @ 2PM

"""


def reverse_binary():
    user_num = int(input())
    new_num = ""
    while user_num > 0:
        new_num += str(user_num % 2)
        user_num = user_num//2
    print(new_num)
    


if __name__ == "__main__":
    reverse_binary()