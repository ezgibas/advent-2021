a_file = open("advent3test.txt", "r")


inpt = []

for line in a_file:

  stripped_line = line.strip()

  #line_list = stripped_line.split()

  inpt.append(stripped_line)


a_file.close()

from collections import Counter
 
def most_frequent(List):
    occurence_count = Counter(List)
    counts = occurence_count.most_common(2)
    if counts[0][1] == counts[1][1]:
        return "1"
    else:
        return counts[0][0]

def least_frequent(List):
    occurence_count = Counter(List)
    counts = occurence_count.most_common(2)
    if counts[0][1] == counts[1][1]:
        return "0"
    else:
        return counts[1][0]

   
# takes in: two strings, one only one character, and an index
# returns a boolean determining if the first character of the long string
# is equal to the small string
def first_digit_equal(binary_num, i, dig):
    return binary_num[i] == dig

# takes in: a string
# returns the first character of the string
def ith_digit(binary_num, i):
    return binary_num[i]

filtered_nums = inpt[:]

i = 0
while len(filtered_nums) > 1:
    iths = list(map(lambda l: ith_digit(l, i), filtered_nums))
    most_freq = most_frequent(iths)
    filtered_nums = [bin_num for bin_num in filtered_nums if first_digit_equal(bin_num, i, most_freq)]
    i += 1

oxygen_generator = filtered_nums[0]
print(oxygen_generator)

i = 0
filtered_nums = inpt[:]
while len(filtered_nums) > 1:
    iths = list(map(lambda l: ith_digit(l, i), filtered_nums))
    least_freq = least_frequent(iths)
    filtered_nums = [bin_num for bin_num in filtered_nums if first_digit_equal(bin_num, i, least_freq)]
    i += 1

co2_scrubber = filtered_nums[0]
print(co2_scrubber)