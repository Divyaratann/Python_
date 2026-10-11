print ("hello")

Name = "Div"
age = 19
cgpa =8.72
is_student = False
print ("My name is", Name, "and I am", age, "years old.")
print(type(Name))
print(type(age))
print(type(cgpa))
print(type(is_student)) 
Name= input("Enter your name:")
print("Hello",Name)
print("Hello " + Name) # concatination 
print("Hello" + " " + Name)
type casting & type conversion
age= input("Enter your age:")
new_age= int(age) + 1
print(new_age)
print(float(new_age))


# #sum of two number

A=input("Enter first number:")
B=input("Enter second number:")
sum=A+B
print("Sum of two number is:",sum)
sum =int(A)+int(B)
print("Sum of two number is:",sum)


name= "div"
Grade= "A"

#string operation
print(name.upper())
print(name.lower())
print(name)

#find
print(name.find("ark"))   #index return krta hai that is position
#agr -1 aya toh m,tlab invalid
print(name.find("v"))   #index return krta hai that is position

#replace
print(name.replace("div","ark"))
print(name.replace("div","surya"))
print(name.replace("div","arru"))


#check for prsence 

print("i" in name)
print("I" in name)

# #reserved word


A= float(input("the price a:"))
B=float(input("the price b:"))
C= float(input("the price c:"))

sum= A+B+C
print("the total price is:",sum)
Avg= sum/3
print("the average price is:",Avg)

name = input("Enter superhero name:")
print("S" in name)


# arithmetic operator
A= int(input("Enter first number:"))
B= int(input("Enter second number:"))
sum1 =A*B
sum2= A+B
sum3= A-B
sum4= A/B
sum5= A//B
sum6= A%B
sum7= A**B

print (sum1)
print (sum2)
print (sum3)
print (sum4)
print (sum5)
print (sum6)
print (sum7)


#assignment operator
cgpa =9.6

x= 1
#x= x+1 #2
x+=2
print(x)

x=2
x = x-1
x-=1
print(x )



#operators precedence
A= 2/2*3
print(A)
A= 2/(2*3)
print(A)


#comparison operator    
print(3>2) #true
print(1>2) #false
print(3<2) #false   
print(3>=2) #true  grweater than or equal to
print(3<=2) #false  less than or equal to
print(3==2) #false
print(2==2) #true      equal to      
print(3!=2) #true  not equal to

#logical operator

#or
# 1 or 0 = 1
str1=3>5
str2= 3<2
print(str1 or str2) #false



# # not 
print(true)
print(not true) #false


# #  and
# # jb dono expression  is true then only it will return true otherwise false

print (3>2 and 3<2) #false
print (3>2 and 3>1) #true



# #conditional statement
age= 24
# #indentation is very important in python
if age>=18:
    print("you are eligible for voting") #spacing is very important in python

elif age<18:
    print("you are not eligible for voting")
print("end of program")

#if else
marks= int(input("Enter your marks:"))
if marks>=80 and marks<=100:
    print("A+")
elif marks>=60 and marks<80:
    print("B+")
else:
    print("C+")
print("program is end")

