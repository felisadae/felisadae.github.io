import collections

g = collections.defaultdict(list)
data = open("airports.txt").read().split()
data = filter(lambda name: len(name) != 3, data)
airport_codes = []
continents = []
for i in range(len(data)):
    if i % 2 == 0:
        airport_codes.append(data[i])
    else:
        continents.append(data[i])
for i in range(len(continents)):
    g[continents[i]].append(airport_codes[i])
print dict(g)
