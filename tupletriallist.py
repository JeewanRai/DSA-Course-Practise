tupletrial = (19, "Python", 12.4, 100)
print(tupletrial)
print(tupletrial[1])
print(tupletrial[-2])

"""can concatenate the tuple like list, tuple is immutable so cannot append new value in the tuple
can perform slicing in the tuple.
can perform length function in tuple"""
tupletrail1 = tupletrial + ("Jeewan Rai", 56.9)
print(tupletrail1)
print(tupletrail1[1:3])
print(len(tupletrail1))

"can perfrom sum function is same kind of data type"
tupl = (10, 23, 33, 100, 394, 1030)
print(sum(tupl))
print(min(tupl))
print(max(tupl))

"Can apply membership operator in the tuple"
print(10 in tupl)