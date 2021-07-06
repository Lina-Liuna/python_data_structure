#string operator:
# +
# *
# in
# len
# str

#string index:
# -6 -5 -4 -3 -2 -1
#  t  o  d  a  y  s
#  0  1  2  3  4  5

#string Slicing
# str[2:5]

#string modify
# str.replace()

#case conversion
#s.capitalize()
#s.lower()
#s.upper()
#s.swapcase()
#s.title()


#find and replace
#s.count(<sub>[,<start>[,<end>]])
#s.endswith(<sub>[,<start>[,<end>]])
#s.find(<sub>[,<start>[,<end>]])
#s.index<sub>[,<start>[,<end>]])Searches the target string for a given substring.


#Character Classification
#s.isalnum() Determines whether the target string consists of alphanumeric characters.
#s.isalpha() Determines whether the target string consists of alphabetic characters.
#s.isdigit()
#s.isidentifier() Determines whether the target string is a valid Python identifier.
#s.islower()
#s.isspace() Determines whether the target string consists of whitespace characters.
#s.istitle()
#s.isupper()

#String Formatting
#s.center(<width>[, <fill>])
#s.expandtabs(tabsize=8)
#s.ljust(<width>[, <fill>])
#s.rjust(<width>[, <fill>])
#s.lstrip([<chars>])
#s.rstrip([<chars>])
#s.strip([<chars>])
#s.replace(<old>, <new>[, <count>])
#s.zfill(<width>)


#Converting between strings and lists
#s.join(<iterable>)
#s.split(sep=None, maxsplit=-1)
#s.rsplit(sep=None, maxsplit=-1)
#s.partition(<sep>)
#s.rpartition(<sep>)
#s.splitlines([<keepends>])


#string operator:
# +
str1 = 'today'
str2 = "is"
str3 = "sunday"
print(str1 + str2 + str3)
# *
print((str1 + "-") * 4)
# in
print("foo" in "food")
# len
print(len(str1))
# str
print(str(123))

#string index:
# -6 -5 -4 -3 -2 -1
#  t  o  d  a  y  s
#  0  1  2  3  4  5

#string Slicing
# str[2:5]
str3 = 'todays'
print(str3[2:5])
print(str3[2:])
print(str3[:5])
print(str3[-1:])
print(str3[-6:-3])

#string modify
# str.replace()
print(str3.replace('o', 'u'))

#case conversion
#s.capitalize() returns a copy of s
# with the first character converted to uppercase and all other characters converted to lowercase:
print("today IS SSunday".capitalize())
#s.lower()
print("THIS IS MY BOOK".lower())
#s.upper()
print("we are happy".upper())
#s.swapcase()
print("Real PYthon".swapcase())
#s.title()
print("start HerE".title())


#find and replace
#s.count(<sub>[,<start>[,<end>]])
print('moo woo boo'.count('oo'))
#s.endswith(<sub>[,<start>[,<end>]])
#s.find(<sub>[,<start>[,<end>]])
#s.index<sub>[,<start>[,<end>]])Searches the target string for a given substring.


#Character Classification
#s.isalnum() Determines whether the target string consists of alphanumeric characters.
#s.isalpha() Determines whether the target string consists of alphabetic characters.
#s.isdigit()
#s.isidentifier() Determines whether the target string is a valid Python identifier.
#s.islower()
#s.isspace() Determines whether the target string consists of whitespace characters.
#s.istitle()
#s.isupper()

#String Formatting
#s.center(<width>[, <fill>])
#s.expandtabs(tabsize=8)
#s.ljust(<width>[, <fill>])
#s.rjust(<width>[, <fill>])
#s.lstrip([<chars>])
print('http://www.realpython.com'.lstrip('htp:/'))
#s.rstrip([<chars>])
print('http://www.realpython.com'.rstrip('on.com'))
#s.strip([<chars>])
print('http://www.realpython.com'.strip('htp:/com'))
#s.replace(<old>, <new>[, <count>])
#s.zfill(<width>)
print('35'.zfill(8))


#Converting between strings and lists
#s.join(<iterable>) Concatenates strings from an iterable.
print(', '.join(['foo', 'bar', 'baz', 'qux']))
print(':'.join('corge'))
print('---'.join(['foo', str(23), 'bar']))

#s.split(sep=None, maxsplit=-1)
print('www.realpython.com'.split('.', maxsplit=1))
print('www.realpython.com'.split('.'))
#s.rsplit(sep=None, maxsplit=-1)

#s.partition(<sep>)
print('foo.bar'.partition('.'))
print('foo@@bar@@baz'.partition('@@'))
#s.rpartition(<sep>)
print('foo@@bar@@baz'.rpartition('@@'))
#s.splitlines([<keepends>])
print('foo\nbar\nbaz\nqux'.splitlines(True))









