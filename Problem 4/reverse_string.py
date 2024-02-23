"""
Complete the following python code to reverse the string entered by the user.

Name: 
Lab Time:
"""

def reverse_string():
    continue_loop = True
    while continue_loop:
        word = input()
        if word in ["done", "Done", "d"]:
            break
        new_word = word[::-1]
        print(new_word)
    

if __name__ == "__main__":
    reverse_string()