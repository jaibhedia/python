m1 = int (input("Enter the marks in the first test: "))
m2 = int (input("Enter the marks in second test: "))
m3 = int (input("Enter the marks in third test: "))
if (m1 > m2):
    if (m2 > m3):
      total = m1 + m2
    else: 
       total = m1 + m3

elif (m1 > m3):
  total = m1 + m2
else:
 total = m2 + m3
 
Avg = total / 2
print ("The average of the best two test marks is: ",Avg)
