numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

print(new_numbers)

name = "Óscar Lopez"
new_name = name.rsplit()

print(new_name)
letters_list = [letter for letter in name]
print(letters_list)

range(1, 5)
double_numbers = [n*2 for n in range(1, 5)]
print(double_numbers)

names = ["Alex", "Beth", "caroline", "Dave", "Eleanor", "Freddie"]

short_names = [item.upper() for item in names if len(item) > 5]
print(short_names)

