"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Mark Zatopek 
Lab Time: Thurs @ 2PM

"""


def reverse_binary(user_input):
    user_num = int(user_input)
    while user_num > 0:
        print(str(user_num%2))
        user_num = user_num//2
    


if __name__ == "__main__":
    reverse_binary(input("Input a number to be converted: "))