import binarytree
import collections

s = ''

c = collections.Counter(s)

print([dict(c)])

x = []

for i in dict(c).keys():
    x.append({i: dict(c).get(i)})


print(x)
print(list(x[0].keys())[0])
for i in range(len(x)):
    for j in range(len(x)-1):
        if x[j].get(list(x[j].keys())[0]) > x[j+1].get(list(x[j+1].keys())[0]):
            x[j], x[j+1] = x[j+1], x[j]

print(list(range(len(x))))

print(binarytree.build(list(range(len(x)))))

print(x)


d = {{}, {} }


# for i in range(len(x)):
#