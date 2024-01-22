def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
ends = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {ends}: ", end="")
for num in range(start, ends + 1):
    if is_prime(num):
        print(num, end=" ")
