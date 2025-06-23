string1 = input("enter the first string = ")
string2 = input("enter the second string = ")

newst = str(string1) + " "+ str(string2)
print(f"the new string is  =\n{newst}")

print(f"\nthe lenght of new string : {len(newst)}")

m1 = input("enter a charcater to perform count,index,find func: " )
print(f"\nnumber of {m1}  is :{newst.count(m1)}")
print(f"number of first occurness at number : {newst.index(m1)}")
print(f" the word {m1} is at this number : {newst.find(m1)}")

print(f"\nthe uppercase for  char in string is = {newst.upper()}")
print(f"the lowercase for  char in string is = {newst.lower()}")
print(f"the capitalized for  char in string is = {newst.capitalize()}")
print(f"the title case for  char in string is = {newst.title()}")
print(f"the swap of upper and lower case in char is = {newst.swapcase()}")

m2 = input("\nwhich char should be replace : ")
m3 = input("which char should be replaced by  : ")
print(f"\nstring after removing whitespace is = {newst.strip()}")
print(f"string after replace {m2} by {m3} is = {newst.replace(m2,m3)} ")

print(f"check if string is num = {newst.isnumeric()}")
print(f"check if string is digits = {newst.isdigit()}")
print(f"check if string is capitalized = {newst.isupper()}")
print(f"check if string is lowercase = {newst.islower()}")
print(f"check if string is titlecase = {newst.istitle()}")
print(f"check if string is letters = {newst.isalpha()}")
print(f"check if string have space = {newst.isspace()}")

m4 = input("\nwhich char should be startswith  : ")
m5 = input("which char should be endswith  : ")
print(f"\ncheck if string is start with {m4} = {newst.startswith(m4)}")
print(f"check if string is end with {m5} = {newst.endswith(m5)}")