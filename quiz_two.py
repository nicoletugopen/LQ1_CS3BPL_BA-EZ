#Perform and print the ff. math opts for all the age and allowances:

student1 = "Nicole T. Bañez"
student2 = "Jerby G. Peralta"
student3 = "Francis Carlo S. De Guia"

#Create Variables that contains their age in whole number
studAge1 = 21
studAge2 = 22
studAge3 = 22

#Create variables that contains their weekly allowance in decimal form
allowance1 = 500
allowance2 = 1000
allowance3 = 1000

nameLen1 = len(student1)
nameLen2 = len(student2)
nameLen3 = len(student3)

print("Member 1 consist of",nameLen1 , "characters")
print("Member 2 consist of", nameLen2, "characters")
print("Member 3 consist of", nameLen3, "characters")

#add the age of members
result1 = studAge1 + studAge2 + studAge3
print(result1)

#subtract the age of all members
result2 = studAge1 - studAge2 - studAge3
print(result2)   

#multiply the age of all the members
result3 = studAge1 * allowance1
result4 = studAge2 * allowance2
result5 = studAge3 * allowance2
print(result3)
print(result4)
print(result5)


#perform and print, compare
compareAge1 = studAge1 -studAge2
compareAge2 = studAge2 - studAge3
print(compareAge1)
print(compareAge2)

#length mem1 -mem2: mem2 to mem3

lengthmem1 = nameLen1 - nameLen2
lengthmem2 = nameLen2 - nameLen3
print(lengthmem1)
print(lengthmem2)

