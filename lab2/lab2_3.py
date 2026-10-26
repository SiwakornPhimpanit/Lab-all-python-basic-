# 03.py - การจัดการข้อมูล List (len, sum, avg, append, insert, pop)
ns = [5, 10, 15, 20, 30]
total = sum(ns)
N = len(ns)
avg = total / N
print("len is", N)
print("total is", total)
print("average is", avg)
print(ns)

ns.append(40) # ต่อท้าย
print(ns)

ns.insert(1, 7) # ตำแหน่ง 1 แทรกค่า 7
print(ns)

ns.pop() # เอาตัวสุดท้าย ออก
print(ns)

ns.pop(1) # เอาตำแหน่งที่ 1 ออก
print(ns)

ns[1] = 5 # เปลี่ยนค่าตำแหน่งที่ 1 เป็น 5
print(ns)