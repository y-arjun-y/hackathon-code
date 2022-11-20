# Q2 - de Bruijn Sequence
# Method - We group the letters according to the length, the first one is just added while the next ones have only their
# last letter added on. If the combination already exists in the result, then we pass in the for loop.

from first_question import res, length  # We import the combinations from the first question

string = "".join(res)
letter_grouping = [string[i:i + length] for i in range(len(string) - 1)]  # We find all the groupings
letter_grouping = letter_grouping[:len(letter_grouping) - length + 1]  # We remove the last element
previous_combs = []  # We add the previous combinations to keep track for the for loop
res_final = ""

for i in range(len(letter_grouping)):
    if i == 0:  # If it is the first combination, we simply add it
        previous_combs.append(letter_grouping[i])
        res_final += letter_grouping[i]
    if letter_grouping[i] in previous_combs:
        previous_combs.append(letter_grouping[i])
        pass
    else:  # If it doesn't already exist, we add the last letter
        previous_combs.append(letter_grouping[i])
        res_final += letter_grouping[i][len(letter_grouping[i]) - 1]

print(res_final)