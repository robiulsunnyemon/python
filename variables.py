x=5; # x is of type int
y="hello, I am a python developer"; #y is of type string
print(x);
print(y);

# multi words variables names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:
        
myNickName="Emon";  #Camel Case
MyNickName="Emon"; #Pascal case
my_nick_name="Emon"; #Snack case

print("----Multi Words Variable Names-----")
print(myNickName);
print(MyNickName);
print(my_nick_name);

# Type casting
a=str(22);
b=int(22.2);
c=float(22);

print("----Type Casting-----");
print(a);
print(b);
print(c);

# Get the Type
number=5;
name="Robiul Sunny Emon";
print("----Get Type Casting-----");
print(type(number));
print(type(name));

# Many values to multiple variables
#Python allows you to assign values to multiple variables in one line:

Id,Department,University= 21111119,"CSE","BSFMSTU";

print("-----------Many values to multiple variables------")
print(Id);
print(Department);
print(University);



# One values to multiple variables
#And you can assign the same value to multiple variables in one line:

mango=guava=banana="fruit Name";

print("-----------One values to multiple variables------")
print(mango);
print(guava);
print(banana);

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

animals=["Cow","Cat","Ant","Tiger"]; #list-tuple
one,two,three,four=animals;
print("-----------Unpack a Collection------")
print(one);
print(two);
print(three);
print(four);


#Global variable && Local variable && global keyword

#Variables that are created outside of a function are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.

#when you create a variable inside a function, that variable is local, and can only be used inside that function.

globalVariable="Global";
def myfunc():
    localVariable="Local";
    global localVariableWithGlobalKeyword;
    localVariableWithGlobalKeyword="Global variable + Global Keyword"
    print("The Global Variable is "+ globalVariable); #global variable call
    print("The Local Variable is "+ localVariable); #Local variable call
    print("The Local Variable with global keyword is "+ localVariableWithGlobalKeyword ); #Local variable call with global keyword

myfunc();

print("The Global Variable is "+ globalVariable + " out side my function"); #global variable is call everywhere

print("The Local Variable with global keyword is " + localVariableWithGlobalKeyword + " out side my function");
