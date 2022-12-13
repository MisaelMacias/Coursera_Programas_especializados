#Write a function called int_return that takes an integer as input and returns the same integer.

def int_return(i):
    return i
z=int(input())
int_return(z)

#Write a function called add that takes any number as its input and returns that sum with 2 added.

def add(x):
    sum = x+2
    return sum
a=int(input())
add(a)

#Write a function called change that takes any string, adds “Nice to meet you!” to the end of 
#the argument given, and returns that new string.

def change(v):
    return v+'Nice to meet you!'

v=input("Enter the string: ")
change(v)

#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.

def accum(lst):
    j=0
    for i in lst:
        j=j+i
    return j
lst=[1,2,3,4,5,6,7,8,9]
accum(lst)

#Write a function, length, that takes in a list as the input. If the length of the list is greater 
#than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.

def length(lst):
    if len(lst)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'

lst=list(input())
length(lst)

#You will need to write two functions for this problem. The first function, divide that takes in any 
#number and returns that same number divided by 2. The second function called sum should take any number, 
#divide it by 2, and add 6. It should return this new number. You should call the divide function within 
#the sum function. Do not worry about decimals.

def divide(n):
    return n/2
def sum(n):
    return n/2+6

sum(divide(10))

#Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.

olympics = ("Beijing", "London", "Rio", "Tokyo")
print(olympics)

#The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple 
#and assign this list to the variable country.

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = [lis[1] for lis in tuples_lst]
print(country)

#With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.

olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

#Define a function called info with five parameters: name, gender, age, bday_month, and hometown. 
#The function should then return a tuple with all five parameters in that order.

def info(name, gender, age, bday_month, hometown):
    z = (name, gender, age, bday_month, hometown)
    return z

#Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far 
#in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. 
#You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

num_medals=[]
for i in gold.items():
    num_medals.append(i[1])