uniques1 = set()
uniques2 = set()
with open('genelist2.txt', 'r') as handle:
    for line in handle:
        uniques1.add(line.rstrip('\n'))

print len(uniques1)

with open('genelist2.txt', 'r') as handle:
    for line in handle:
        uniques2.add(line.rstrip('\n'))

print len(uniques2)

for x in uniques1:
    if x not in uniques2:
        print x
for x in uniques2:
    if x not in uniques1:
        print x
