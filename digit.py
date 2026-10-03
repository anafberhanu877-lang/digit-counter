i = int(input("Enter a number: "))

num = 0

while i > 0:
    i = i // 10
    num = num + 1

print("The number has", num, "digits")