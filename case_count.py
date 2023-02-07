lower=0
upper=0
d=open('sample.txt', 'r')
data=d.read()
lines = data.split()
for word in data:
    if word.islower():
        lower += 1
    if word.isupper():
        upper += 1
print("Number of lowercase:",lower)
print("Number of uppercase:",upper)
