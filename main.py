
#1. for loop
#for i in range(0,5):
#print(i)

#2. print String
#print('I am a student')
#print("I am learning python")


#3. print integer
#print(3+2)
#print((3+2)+5)

#4. Variable
#number=3+2
#new_number=number+5
#print(number)
#print(new_number)

#5. Data Type
#name="Karim"
#age=63
#print(name)
#print(age)
#print(str(21)+name)
#print(type(name))
#print(type(age))

#6. Ratio
#ratio=2.5
#print(type(ratio))

#7. Taking Input
#print("What is your name?")
#print("Your name please:")
#name = input()
#print(f"Hi {name},Congratulations!")

#8. variables
#print("Hello World")
#fruits = "mangos"
#print(fruits)
#fruits = "apples"
#print(fruits)

#9.Add Data types
#x=5
#y=3.5
#print(x+y)
#w=True
#z=False
#print(w)
#print(z)

#10. Arithmetic Operators
#print(10 - 7) #Substraction
#print(10 + 7)#Addition
#print(10 * 7)#Multiplication
#print(10 ** 7)#Exponent
#print(10 / 7)#division
#print(10 // 7)#div result round figure ie, Floor division
#print(10 % 7)#Remainder

#11. Assignment Oprator
#x=3
#y=4
#print(y + x)
#print(y-x)
#print(y*x)
#print(y**x)
#print(y/x)
#print(x/y)
#print(x//y)
#x+=y #ie,x=x+y
#print(x)

#12. Comparision Operator true and false
#x=10
#y=20
#print(x!=y)#unequality
#print(x==y)#Equality
#compare=x>y#check x>y

#print(compare)
#compare=x<y #check x<y
#print(compare)

#13. Logical Operator and, or ,not

#And Operator truth table
#TT=True
#FF=False
#TF=False
#FT=False
#x=15
#y=25

#logical_and=x<y and y>x
#print(logical_and)

#logical_and=x>y and x==y
#print(logical_and)

#logical_and=x>y and y>x
#print(logical_and)

#logical_and=x<y and x==y
#print(logical_and)

#OR Operator truth table
#FF=False
#TT=True
#TF=True
#FT=True
#x=15
#y=25

#logical_or=x>y or x==y
#print(logical_or)

#logical_or=x<y or y>x
#print(logical_or)

#logical_or=x<y or x==y
#print(logical_or)

#logical_or=x>y or y>x
#print(logical_or)

#not Operator truth table
#false convert true
#true converts false

#x=15
#y=25

#logical_not=not x==y
#print(logical_not)

#logical_not=not x<y
#print(logical_not)

#14.Types of number: integer, float, string and boolean
#w= True
#x= 22/7
#y= 22
#z= "22"
#print(type(w))
#print(type(x))
#print(type(y))
#print(type(z))

#15. methods
#syntax-- round(number,digit)
#pi=3.141592653589793238
#print(round(pi,4))
#print(round(pi,2))

#16. Using exponant or power
#syntax--pow(base,exponent)
#x=pow(2,5)
#print(x)

#17. Getting absolute value
#x=abs(-7)
#print(x)
#18.Reminder: syntex---divmod(vaijjo,vajok) result(vagfol, remainder)

#x=divmod(23,5)
#print(x)

#19. String method Single quote and Double quote
#text='Hi,I am karim.I love "python"Programming.'
#print(text)

#text="Hi,I am karim.I love 'python'Programming."
#print(text)

#20. Multi line string
#text='''Python is easy to learn.
#Python is one of the easy language.
#Are you sure having fun?'''
#print(text)

#21. Concatinating string
#a="Hello "
#b="World!"
#text=a+b
#print(text)

#22. Accessing part of string
#Using indexing

#text="I LOVE PYTHON"
#print(text)
#print(text[0])
#print(text[2])
#print(text[3])
#print(text[4])
#print(text[5])

#23. String slicing
#text="Python"
#print(text[2:6])

#24. String method
#Capitalizing, Uppercase, Lowercase
#name="md. Abdul Karim"
#x=name.capitalize() #Only 1st charecter upper and others lower
#print(x)
#x=name.upper() #Hole sentence upper
#print(x)
#x=name.lower() #Hole sentence lower
#print(x)
#print(len(name)) #Length of string
#Replacing string value --Syntex("old word","new word")
#text="Hello World!"
#print(text)
#y=text.replace("World","Firoz")
#print(y)

#25. input function
#name=input("Enter your name: ")
#print("I am ",name)
#num1=input("Enter num1: ")
#num2=input("Enter num2: ")
#x=int(num1)+int(num2)
#print(x)
#26. List in python(arry) list is ordered container
#pets=["cat","dog","cow","rabbit"]
#print(pets)
#(+)ve indexing  0,    1,    2,      3
#               cat,  dog,  cow,   rabbit
#(-)ve indexing -4,   -3,   -2,     -1
#cat[-4],dog[-3],cow[-2],rabbit[-1],cat[0],dog[1],cow[2],rabbit[3]
#print(pets[-4])
#print(pets[-3])
#print(pets[-2])
#print(pets[-1])
#print(pets[0])
#print(pets[1])
#print(pets[2])
#print(pets[3])

#27. range of index
#print(pets[1:3])
#print(pets[0:3])

#28. Adding item to a list
#append method
#print(pets)
#pets.append("elephant")
#print(pets)
#29. insert method
#pets.insert(0,"rat")
#print(pets)
#print(pets[0])
#print(pets[4])
#remove method
#30. pets.remove("cow")
#print(pets)
#31. Length of the list
#print(len(pets))
#32. Changeing an Item of list
#pets[2]="fish"
#print(pets)
#33. extending or merge two lists
#num1=[1,2,3]
#num2=[4,5,6,7]
#num1.extend(num2)
#print(num1)
#34. delete last item
#print(pets)
#pets.pop()
#print(pets)
#delete last item
#pets.pop()
#print(pets)
#delete last item
#pets.pop()
#print(pets)
#remove method
#print(pets)
#pets.remove("dog")
#print(pets)
#35. membership operator in and not in
#country=["Bangladesh","India","Pakisthan","England","Australia"]
#check_item="India" in country
#print(check_item)
#check_item="Norway" in country
#print(check_item)
#check_item="Bangladesh" not in country
#print(check_item)
#check_item="Shrilanka" not in country
#print(check_item)
#36. Multi data type item remain in an array
#mixture=[2,2.5,"Firoz",True,False]
#print(mixture)
#37. tuple
#country=("Bangladesh","India","Pakisthan","England","Australia")
#print(type(country))
#country[1] = "Norway"
#print(country)
#Can't change tuple item
#38. function
#Declearing function

#def hello_world():
    #function body which is execute
    #print("Hello Karim!")
#out of function
#calling function re useable
#hello_world()
#hello_world()
#hello_world()
#hello_world()
#hello_world()

#39. function
# Parameter(variable where declear in function ie,name) 
# Argument(value of variable where calling function)

#Declearing function using one parameter

#def hello_world(name):
    #function body which is execute
  #x= "Hello "+ name
  #print(x)
#out of function
#calling function re useable using different Argument(value)
#hello_world("Firoz")
#hello_world("Faruk")
#hello_world("Farid")
#hello_world("Miru")
#hello_world("Beru")

#40.Project-1: two integer using function
"""
def add_number(num1,num2):
    sum = num1 + num2
    print(sum)

    sub = num1 - num2
    print(sub)

    mul = num1 * num2
    print(mul)

    div = num1 / num2
    print(div)

    exp = num1 ** num2
    print(exp)

    rem = num1 % num2
    print(rem)

add_number(4,3)
"""
#project-2
"""
# if statement
x=30
y=20
#if statement
if x<y:
    #Body of if statement
    print("x is smaller than y")
else:
    #Body of else part
    print("x is grater than y")
"""
#project-3
"""
#Multiple condition
x=-20
y=20
#if statement
if x<y:
    #Body of if statement
    print("x is smaller than y")
elif x>y:
    #The body of elif part
    print("x is grater than y")
elif x==y:
    #Body of elif part
    print("x is equal to y")
else:
    #Body of else part
    print("Enter right value")
"""