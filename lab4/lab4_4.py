# lab4_4.py: สร้างฟังก์ชัน lenv3 คำนวณความยาวของเวกเตอร์ 3 มิติ
import math

def lenv3(v):
    sumofPower2 = v[0]*v[0] + v[1]*v[1] + v[2]*v[2]
    lena = math.sqrt(sumofPower2)
    return lena

a = (1, 2, 3)
b = (3, 0, 0)

lena = lenv3(a)
lenb = lenv3(b)

print(f"Lenght of vector a = {a} is {lena}. ")
print(f"Lenght of vector b = {b} is {lenb}. ")

