#dictionary are indexed by keys, which can by any immutable type, strings and numbers can always be keys.
#tuples can be used as keys if they contain only strings, numbers or tuples
# a set of key:value pairs, with the requirement that the keys are unique(within one dictionary).
# performing list(d) on a dictionary returns a list of all the keys used in the dictionary.

# to check whether a single key is in the dictionary, use the in keyword.

dic1 = {x: x**2 for x in (2, 4, 6)}
print(dic1)
print(list(dic1))
for k, v in dic1.items():
    print(k, v)