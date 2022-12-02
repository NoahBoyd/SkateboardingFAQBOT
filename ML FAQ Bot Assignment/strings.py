"""
Some simple String processing examples.

A string is a list of characters. Many list processing methods work on strings
as well.

BUT!!! Strings are immutable (unchangeable). For example, s.lower() returns
a lowercase copy of s but leaves s unchanged. Use s=s.lower() to replace s with
the lowercase version. Also s[6]="Q" is illegal and throws a runtime error.

Sam Scott, Mohawk College, 2021
"""

s = "  The quick, Brown fox jumps over the lazy dogs.\n\n"

print("s:",s)
s=s.strip()
print("s=s.strip():",s)
print("s.lower():",s.lower())
print("s.upper():",s.upper())
print("s.count('s'):",s.count("s"))
print("s.endswith('dogs.')",s.endswith("dogs."))
print("s.startswith('dogs.')",s.startswith("dogs."))
print("s.find('fox'):",s.find("fox"))
print("s.split():",s.split())
print("s[11]:",s[11])

print("String processing: ", end="")
for char in s.upper():
    if char.isalpha():
        print(char,end="")
print()

print()
print("**** Also check out isdigit, isalpha, replace, and many other string methods.")
print("**** To do that, just type s. below")
