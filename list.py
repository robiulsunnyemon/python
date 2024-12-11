student=["Durjoy","Leon","Orgho","Sammo","Tayeb","Akhash","Rifat","Mukter","Noman","Sakib"]; #list of student
marks=[70,67,65,88,31,33,99,95,77,88,61]; #list of marks

print(student);
print(marks);
print(student[1]); #print Leon
print(marks[1]); #print 67

#List method
#append list
student.append("siddique"); #add siddique
print(student);

print("length of array is:", len(student)); #find length
marks.sort(); #sorting marks accending
print(marks);

marks.sort(reverse=True); #sorting marks decending
print(marks);

#sliding list
print("Sliding marks", marks[4:7]); #print marks[4],[5],[6]
print(marks[4:]); #print marks[4] unit marks[len(marks)-1]
print(marks[:7]); #print marks[0] until marks[6]
print(marks[-5:-1]); #print marks[len(marks)-5]......marks[len(marks)]

#reverse list
Roll=[70,67,65,88,31,33,99,95,77,88,61]; #list of marks
Roll.reverse()
print(Roll)

#add list
Teacher=["DMA","MHK","SR","MH","MSR","MKU"]
print(Teacher);
Teacher.insert(0,"First Teacher");
print(Teacher);
Teacher[0]="1st Teacher";
print(Teacher);
Teacher[len(Teacher)-1]="Last Teacher";
print(Teacher)
Teacher[2:5]="Missing Teacher","Mising Teacher1","Missing Teacher2";
print(Teacher);


#extend

student.extend(marks);
print(student);

marks.extend(Teacher);
print(marks);

print(marks);

marks.remove(99); #remove value 99
print(marks);

marks.pop(3); #remove value of index3
print(marks);


#clean blank marks
marks.clear() 
print(marks) #print blank


