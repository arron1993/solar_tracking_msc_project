big = open('./All/06092016_F.csv', 'r')
small = open('./Reduced/F_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
big.close()
small.close()
big = open('./All/06092016_DAS.csv', 'r')
small = open('./Reduced/DAS_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
big.close()
small.close()
big = open('./All/06092016_DAT.csv', 'r')
small = open('./Reduced/DAT_REDUCED.csv', 'w')

lines = big.readlines()
reduced = []
counter = 0
for line in lines:
    if counter % 100 == 0:
        small.write(line)
    counter+=1
big.close()
small.close()