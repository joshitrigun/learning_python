from collections import Counter
import re


description = """
Python is an easy to learn, powerful programming language. 
It has efficient high-level data structures and a simple but effective approach 
to object-oriented programming. Python’s elegant syntax and dynamic typing, 
together with its interpreted nature, make it an ideal language for scripting 
and rapid application development in many areas on most platforms
 """

# words = description.split()
# print(words)

words = re.findall('\w+', description)

dic1 = Counter(words)
print(dic1.most_common(3))