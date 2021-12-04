a_file = open("advent3input.txt", "r")


inpt = []

for line in a_file:

  stripped_line = line.strip()

  #line_list = stripped_line.split()

  inpt.append(stripped_line)


a_file.close()

#print(inpt)

firsts = []
seconds = []
thirds = []
fourths = []
fifths = []
sixths = []
sevenths = []
eighths = []
ninths = []
tenths = []
elevenths = []
twelveths = []

for num in inpt:
  firsts.append(num[0])
  seconds.append(num[1])
  thirds.append(num[2])
  fourths.append(num[3])
  fifths.append(num[4])
  sixths.append(num[5])
  sevenths.append(num[6])
  eighths.append(num[7])
  ninths.append(num[8])
  tenths.append(num[9])
  elevenths.append(num[10])
  twelveths.append(num[11])

lol = [firsts, seconds, thirds, fourths, fifths, sixths, sevenths, eighths, ninths, tenths, elevenths, twelveths]

from collections import Counter
 
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

gamma = ""

for l in lol:
  gamma += most_frequent(l)

print(gamma)
   

