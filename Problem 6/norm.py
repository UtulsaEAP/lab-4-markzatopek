"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:
Lab Time:
"""

def norm():
    total_values = int(input())
    if total_values < 1:
        return
    values = []
    adjusted_values = []
    for _ in range(total_values):
        values.append(float(input()))
    
    max = values[0]
    for value in values:
        if value > max:
            max = value
    
    for value in values:
        print(f"{(value / max):.2f}")
    
    

if __name__ == "__main__":
    norm()