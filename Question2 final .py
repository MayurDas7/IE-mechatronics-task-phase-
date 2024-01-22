n=int(input('Enter no. of entries:'))
names = []
for i in range(n):
    a=input('Name:')
    names.append(a)

# Process the names
processed_names = []
for name in names:
    # Split the name at the first space
    parts = name.split(" ", 1)
    # Capitalize all letters in the first part
    first_part = parts[0].upper()
    # If there's a second part, lowercase all letters in it
    if len(parts) > 1:
        second_part = parts[1].lower()
        processed_name = f"{first_part} {second_part}"  # Add a space back
    else:
        processed_name = first_part
    # Remove spaces and last two letters
    processed_name = processed_name.replace(" ", "")[:-2]
    processed_names.append(processed_name)

# Sort the processed names in ascending order
processed_names.sort()

# Print the processed names with indexing
for i, name in enumerate(processed_names):
    print("{}. {}".format(i+1, name))

