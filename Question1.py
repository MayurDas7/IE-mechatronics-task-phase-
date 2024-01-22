target_sum = int(input("Enter Number:"))

for x in range(target_sum + 1):
    for y in range(target_sum + 1 - x):
        z = target_sum - x - y
        print(f"x = {x}, y = {y}, z = {z}")