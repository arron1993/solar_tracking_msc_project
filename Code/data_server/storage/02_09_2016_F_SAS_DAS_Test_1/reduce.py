big = open('./All/02092016_F.csv', 'r')
small = open('./Reduced/F_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1

big = open('./All/02092016_SAS.csv', 'r')
small = open('./Reduced/SAS_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1

big = open('./All/02092016_DAS.csv', 'r')
small = open('./Reduced/DAS_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
