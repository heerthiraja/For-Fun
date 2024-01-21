print("Hello World")

#Numbers
print(10)
print(2.5)
print(5+2j)
print(555+555)
print(500-100)
print(500*2)
print(500/5)
print(3 ** 3)
print(3%2)

#Variables
watch= 500
print(watch)
#loo=print(watch+100)
#print(loo)

customer_name= "Karthik"
Watch1,Watch2 = 750,250
print(Watch1), print(customer_name)
# print( customer_name + Watch1) - This gives error. bcoz CN is a string. we cant add it.

#Strings So Important. Used in everything.
word= 'hi dude'
word2= '     hello everyone. Its 100!'
print(word)
print(word2)
# """ is used to write something more than 1 line.
para= """This
is
Heerthi"""
print(para)
#string can be used as array too.

#every single letter or number is an array. count as an array.
word3= "Hello"
print(word3[0]); print(word3[1]), print(word3[2]), print(word3[3]), print(word3[4])

#Slicing
#print(word3[0:5])
print(word3[-5:-1])
print(len(word3))
print(len(para)) #we can find length with len.
print(word2.strip()) #strip is to remove gaps.
print(word.upper()) #this is make it Caps.
print(word.lower()) #to make is Lower case.

a='raj'
print(a.replace('j','ja')) #WE CAN REPlace the words, numbers.
# a. after this, you can find more str functions. try it one by one.
print(a.split('a'))
print("Hell" in word3) # Theese are booleans. True or false. thats it.

a1 = 'heerthi'
a2= ' raja'
print(a1+a2) #adding 2 variables

#Operators

print(1>10)  #boolean
# Operators - arithmetic ,=,> < >= <=  and or not   is is not   in not in & | ^ ~ << >>

number1 =10
number2 = number1 + 10
print (number1, number2)

#casting
a= 10 #integer
b= int(10.10) #we are changing decimal into integer. this is casting.
print(a, b) #we can make a float as int, int as float. that is casting.

 #List
fruits = ['apple', 'orange', 'cherry'] # In list we can save a lot of thing in one variable.
print(fruits)
print(fruits[0]), print(fruits[1])
fruits[1]= 'banana' #we can change.
print(fruits)
print(len(fruits))
# fruits.  we can see many. try it one by one.
fruits.append("new") # we can add variables or str with append.
print(fruits) #m is methods. f is fields

#Tuples #list and tuples have similar thing.
#tuples have []  list use () , we cant change anything in tuples.

#Sets This also similar to tuples. for set {} braces. #game deve used. it changes random. It has no index.

game= {'banu', 'seenu', 'thenu'}
print(game)

#Dictionary
my_data = {
    "name": "Heerthi",
    "age": "19"
}
print(my_data)
print(my_data.get("age"))
my_data["age"] = "20"  #try the methods and fields one by one.

#If, Elif, Else

age = 18
if age>18:
    print("You can do anything")
elif age==18:
    print("You have full Freedom")
else:
    print(" There is no Limit for Anything")

#and or
a,b = 10,20 #it print if everything is same.
if a==10 and b==10:
    print("Correct")
else:
    print("Incorrect")

a,b = 10,20 #If shows even anyone is crt.
if a==100 or b==20:
    print("Correct")
else:
    print("Incorrect")

#Nested If

a,b = 10,20
if a==10 or b==20:
    print("Correct")
    if b==20:
        print("Good")
else:
    print("Incorrect")

#functions , we can use a code repeatedly with functions.

'''def addition():
    a=5
    b=10
    print(a+b)
addition()''' #this is the function name to call.

def add(a,b):
    print(a+b)
add(20,10)

#return
def fun(a):
    return a*100
print(fun(5))

#loops If we want to repeat something. we can use loop. this is same like function?
# one time write and use again is function. writing one time and use many times is loops. name itself having its meaning.

#for Loop
name = 'Heerthi'

for letters in name:
    print(letters)

fruits = ['apple','guva', 'pine']

for fruit in fruits:
    print(fruit) #we can use if condition in for loop.
# To stop running code, we can use 'break'.

#range
'''for number in range(5):
    print(number)''' #if we use range. we can see the list till the number u mention.
# to get from specific;
'''for number in range(2,10):
    print(number)'''
for number in range(2,8,2):
    print(number)
else:
    print("everything finished")

#while loop
i=1
while i<5:
    print(i)
    i +=1
else:
    print("Over")

#Lambda function
add_5 = lambda number: number+10
print(add_5(10)) #we can use big thng with single line of code with lambda.

#input, this is the main thing. like we are going to do practical thing. collect thing from user, etc.

'''number1=10
number2=12
print(number1+number2)'''

#name= input("Your Name") #all data we collect form input saved as string.
#print("My name is"+ name)

#simple Calci

def addi(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(""" Select Operation
1. add
2. sub
3. mul
4. div
""")

#choice = int(input("Enter your choice"))
#a= int(input("Enter the number"))
#b= int(input("Enter the number"))
'''if choice ==1:
    print(add(a,b))
elif choice ==2:
    print(sub(a,b))
elif choice ==3:
    print(mul(a,b))
elif choice==4:
    print(div(a,b))
else:
    print("Enter correct choice")
'''
#Task for Me

print( "Hi, I can code in Python!")

print("My favourite animal is dog")

print(""" 
o-###-
  ||    #
""")

print("This is my home")

print("""
  _|_
 |   |
 |#  |____
 |   |    |
 | # |  # |  
_|___|_#__|_   
""")

print("Now puzzle time")
year= int(input("What year yere you born?"))
if year<=2025:
    print ("In the year 2025 you'll be 21 years old!")
else:
    print("Good Bye!")

print("THANK YOU!")