big = open('./ALL_CSVs/DAT_ALL.csv', 'r')
small = open('./REDUCED_CSVs/DAT_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
