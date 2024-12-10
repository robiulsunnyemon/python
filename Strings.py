#string are arrays
greeting="Good Night";
print(greeting[0]);

#print using loop
for i in greeting:
    print(i);

print("length is :", len(greeting)); #print length

#Check String
#Check if "Good" is present in the above greeting variable:
print("Good" in greeting);
print("moring" not in greeting);


#indexing call
print(greeting[2]);
print(greeting[5]);

#slicing call
print(greeting[2:6]); #print greeting[2],[3],[4],[5],[6]
print(greeting[2:]); #print  start greeting[2] and until end
print(greeting[:5]); #print  start greeting[0] and until greeting[5]

#negative slicing
print(greeting[-5:-1]);


#Modify Strings
print(greeting.upper()); #modify string
print(greeting.lower()); #Lower string
#remove white space
print(greeting.strip()) # Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(greeting.replace("Night","Morning")) #Replace String
greeting1=greeting.split(" "); #split string
print(greeting1);

#string concatenation

name="Robiul Sunny";
nickName=" Emon";
age=22;

nameAndNickName=name+nickName;
print(nameAndNickName + " age is", age);