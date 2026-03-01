
from collections import Counter


s=input("enter the string: ")
t=input("enter the string: ")

def anagram(s,t):
    return Counter(s)==Counter(t)

if anagram(s,t):
    print(s,"and",t,"are anagrams")
else:
    print(s,"and",t,"are not anagrams")