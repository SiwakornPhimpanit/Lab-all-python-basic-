# lab4_3.py: สร้างฟังก์ชัน dotv3 คำนวณ Dot Product ของเวกเตอร์ 3 มิติ

def dotv3(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

a = (1, 2, 3)
b = (1, 0, 1)
c = (1, 2, 4)

dotab = dotv3(a, b)
dotac = dotv3(a, c)

print(f"dot of vector a and b = {dotab}")
print(f"dot of vector a and c = {dotac}")

