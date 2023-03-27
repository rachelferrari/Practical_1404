# 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# # 2
in_file = open("name.txt")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# 3
in_file = open("numbers.txt", "r")
numbers = in_file.readlines()
in_file.close()
total = int(numbers[0]) + int(numbers[1])
print(total)

# #4
NUMBERS_FILE = "numbers.txt"
total = 0
in_file = open(NUMBERS_FILE, "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)
