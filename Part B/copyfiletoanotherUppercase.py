
f1 = open("samplefile.txt", "r")
# To open the second file in append mode
f2 = open("samplefile1.txt", "a")
 
# For loop to traverse through the file
for line in f1:
 
 # Writing the content of the first
 # file to the second file
 
 # Using upper() function
 # to capitalize the letters
 f2.write(line.upper()) 