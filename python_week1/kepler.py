def kaprekar_steps(num, count=0):
    if num == 6174:
        return count
    
    digits = list(str(num))
    digits.sort()
    asc = int("".join(digits))
    desc = int("".join(digits[::-1]))
    result = desc - asc

    return kaprekar_steps(result, count + 1)
n = int(input("Enter a 4-digit number: "))
steps = kaprekar_steps(n)
print(f"Steps to reach 6174: {steps}")
