#Data Storage, Strings and Printing
#Create a Variables that store the names of your groupmates

student1 = "Nicole T. Bañez"
student2 = "Jerby G. Peralta"
student3 = "Francis Carlo S. De Guia"

#Create Variables that contains their age in whole number
studAge1 = str(21)
studAge2 = str(22)
studAge3 = str(22)
#Create variables that contains their weekly allowance in decimal form

allowance1 = float(500)
allowance2 = float(1000)
allowance3 = float(1000)

# Print all results formated as follows: use concat
print(student1, student2, student3, studAge1, studAge2, studAge3, allowance1, allowance2, allowance3)

#Teamname: Member 1: StudentName, his/her age is "age", allowance per week is "allowance"
teamName = "JANGGO"
print("TEAM NAME:",teamName)
print("Member 1:", student1, "her age is", studAge1, "and her allowance per week is", allowance1)
print("Member 2:", student2, "his age is", studAge2, "and his allowance per week is", allowance2)
print("Member 3:", student3, "his age is", studAge3, "and his allowance per week is", allowance3)

#Create variables to store the length of the names of the members 
nameLen1 = len(student1)
nameLen2 = len(student2)
nameLen3 = len(student3)

#Print the length of the members
print("Member 1 consist of",nameLen1 , "characters")
print("Member 2 consist of", nameLen2, "characters")
print("Member 3 consist of", nameLen3, "characters")
