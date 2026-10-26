import math

a = (1,0, 0)
sumofPower2 = a[0]*a[0] + a[1]*a[1] + a[2]*a[2]
lena = math.sqrt(sumofPower2)
lena = round(lena, 2) 
print(f"Lenght of vector a = {a} is {lena}. ")