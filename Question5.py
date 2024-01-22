n=5
names = []
numbers = []
result_dict = {}
for i in range(5):
    name = input("Enter a name: ")
    number = int(input("Enter a number: "))
    names.append(name)
    numbers.append(number)

sorted_names = sorted(names)
sorted_numbers = sorted(numbers)

for i in range(n):
    result_dict[sorted_names[i]] = sorted_numbers[i]


print("Output:",result_dict)