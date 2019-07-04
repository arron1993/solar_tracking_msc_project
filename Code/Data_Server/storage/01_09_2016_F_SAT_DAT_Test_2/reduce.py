big = open('./All/F_ALL.csv', 'r')
small = open('./Reduced/F_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1

big = open('./All/SAT_ALL.csv', 'r')
small = open('./Reduced/SAT_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1

big = open('./All/DAT_ALL.csv', 'r')
small = open('./Reduced/DAT_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
