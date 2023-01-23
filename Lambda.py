# 1. Lambda with if but without else in Python
square= lambda x: x*x if (x > 0) else None
print(square(4))
print(square(12))
#2 Python | Sorting string using order defined by another string
# 3 Python program to count Even and Odd numbers in a List
list1 = [10, 21, 4, 45, 66, 93, 11]
odd_count = len(list(filter(lambda x: (x % 2 != 0),list1)))
even_count = len(list(filter(lambda x : (x % 2 == 0),list1)))
print('Even numbers in list',even_count)
print('Oddd numbers in list',odd_count)
# 4 Python | Find the Number Occurring Odd Number of Times using Lambda expression and reduce function
from functools import reduce
def odd_times(x):
    print(reduce(lambda a, b : a ^ b, x))

if __name__ == "__main__":
    x = [1,2,3,2,3,1,3]
    odd_times(x)
# 5 Python – Lambda Function to Check if value is in a List
list1 = [1,2,3,4]
number = 5
x = lambda list1,number: True if number in list1 else False
if (x(list1, number)):
    print('Element is present in list')
else:
    print("Element is not present in list")
#6 Python: Iterating With Python Lambda
list1 = [4,2,13,21,5,10,25]
list2 = []
for i in list1:
    result = lambda i : i**2
    list2.append(result(i))
print('The square of gven list is',list2)
# check if two numbers is equal or greater or lesser
result = lambda x,y: f"{x} is smaller than {y}"\
        if x < y else (f"{x} is greater than {y}" if x > y \
                       else f"{x} is equal to {y}")
print(result(12,11))
print(result(12,12))
print(result(12,13))
# 8 Python – Lambda function to find the smaller value between two elements
# method 1
minimun = lambda a,b : min(a,b)
print(minimun(10,5))
print(minimun(12,85))
# method 2
minimum = lambda a,b : a if a < b else b
print(minimum(100,105))
print(minimum(200,190))
# 9 Overuse of lambda expressions in Python
x1 = (lambda x,y,z: (x + y) * z,(1,2,3))
print(x1)
x2 = (lambda x,y,z:(x + y) if (z == 0) else (x * y),(1,2,3))
print(x2)
# 10 Intersection of two arrays in Python ( Lambda expression and filter function )
def intersection(arr1,arr2):
    result = list(filter(lambda x: x in arr1,arr2))
    print('Intersection :',result)
if __name__ == "__main__":
    arr1 = [1,3,4,5,7]
    arr2 = [2,3,5,6]
    intersection(arr1,arr2)
# Map function and Lambda expression in Python to replace characters
def replace_chars(input,c1,c2):
    newchars = map(lambda x : x if (x!= c1 and x!=c2) else\
                   c1 if (x == c2) else c2, input)
    print("".join(newchars))
if __name__=="__main__":
    input = "grrksfoegrrks"
    c1 = "e"
    c2 = "r"
    replace_chars(input,c1,c2)
# lambda filter examples
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]
result = list(filter(lambda x : (x % 13 == 0),my_list))
print(result)
# Given a list of strings, find all palindromes.
my_list = ["geeks", "geeg", "keek", "practice", "aa"]
result = list(filter(lambda x: (x == "".join(reversed(x))),my_list))
print(result)
#Given a list of strings and a string str, print all anagrams of str
# Lambda expression in Python to rearrange positive and negative numbers
def rearrange(arr):
    return [x for x in arr if x < 0]+[x for x in arr if x > 0]
if __name__ == "__main__":
    arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(rearrange(arr))
#Ways to sort list of dictionaries by values in Python – Using lambda function
list1 = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]
print('Print dict using sorted age')
print(sorted(list1,key=lambda i: i['age']))