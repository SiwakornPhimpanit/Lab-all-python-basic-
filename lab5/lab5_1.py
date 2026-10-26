# lab5_1.py: วาดกราฟจุดและกราฟเส้นสุ่ม (Cell 10)
import matplotlib.pyplot as plt
import random

xs = []
ys = []
random.seed(2)
for i in range(10):
    x = i + 1
    y = random.randint(0, 100)
    xs.append(x)
    ys.append(y)

print("xs =", xs)
print("ys =", ys)

print("Thunyarat")

plt.scatter(xs, ys)
plt.plot(xs, ys, color='red')
plt.title("Random Data Line Plot - Thunyarat")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
