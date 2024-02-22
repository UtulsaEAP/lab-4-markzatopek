"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:
Lab Time:
"""

def password_mod():
    word = input()
    password = ''
    
    new_word = word.replace('i' , '1').replace('a', '@').replace('m', 'M').replace('B', '8').replace('s', '$')
    
    password = new_word

if __name__ == "__main__":
    password_mod()