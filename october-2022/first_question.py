# Q1 - Write a program to input 2 characters and a length. The code should display all possible combinations of given
# length.
# Method: We input both characters from the user, calculate the length and find the last binary code using all 1's of
# the given length.
# After that, we calculate all the binary codes in the range between 0 and the last binary code.
# Finally, we replace all the 0's with the first character inputted and all the 1's with the second_character inputted

first_character = input("Enter 1st character: ")
second_character = input("Enter 2nd character: ")
length = int(input("Enter length: "))

last_binary_code = int('1'*length, 2)  # We get the last binary code
temp = []
res = []

for i in range(0, last_binary_code+1):
    a = bin(i)[2:]
    if len(a) != length:
        a = '0'*(length-len(a)) + a  # We add padding if it is not of equal length
    temp.append(a)

for i in temp:
    string = i
    string = string.replace('0', first_character)  # We replace the 0s with the first character
    string = string.replace('1', second_character)  # We replace the 1s with the second character
    res.append(string)

print(res)
